use rand::Rng;

const A: u64 = 1664525;
const C: u64 = 1013904223;
const M: u64 = u64::MAX;   // 2^32

fn lcg(seed: u64) -> impl Iterator<Item = u64> {
    let mut x = seed;
    std::iter::from_fn(move || {
        x = (A.wrapping_mul(x).wrapping_add(C)) % M;
        Some(x)
    })
}

fn histogram(nums: &[u64], buckets: usize) -> Vec<usize> {
    let mut hist = vec![0usize; buckets];
    for &n in nums {
        let b = ((n as f64 / M as f64) * buckets as f64) as usize;
        let idx = if b >= buckets { buckets - 1 } else { b };
        hist[idx] += 1;
    }
    hist
}

fn runs_test(nums: &[u64]) -> usize {
    let mut runs = 1;
    for i in 1..nums.len() {
        if nums[i] > nums[i - 1] {
            if nums[i - 1] <= nums.get(i - 2).unwrap_or(&nums[0]) {
                runs += 1;
            }
        }
    }
    runs
}

fn main() {
    // 1. Generate 10,000 numbers
    let numbers: Vec<u64> = lcg(777).take(10_000).collect();

    // 2. Histogram
    let hist = histogram(&numbers, 20);
    println!("Histogram (20 buckets): {:?}", hist);

    // 3. Runs Test
    let r = runs_test(&numbers);
    println!("Runs test result: {r}");

    // Interpretation hints
    println!("High uniformity means histogram buckets are similar size.");
    println!("Runs test should show randomness (not too few or too many runs)");
}