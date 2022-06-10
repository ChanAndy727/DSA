let i = 1;
var findKthLargest = function(nums, k) {
    // if (i === k) {
    //     return Math.max(...nums);
    // } else {
    //     i++;
    //         let arr = nums.filter(num => num !== Math.max(...nums));
    //         return findKthLargest(arr, k);
    // }
    for (let i = 0; i < k; i++) {
    let max_index = i;
    let tmp = nums[i];

    for (let j = i + 1; j < nums.length; j++) {
      if (nums[j] > nums[max_index]) {
        max_index = j;
      }
    }

    nums[i] = nums[max_index];
    nums[max_index] = tmp;
  }

  return nums[k - 1];
};