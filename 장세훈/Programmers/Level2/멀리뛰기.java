class 멀리뛰기 {
    /*
        https://school.programmers.co.kr/learn/courses/30/lessons/12914
     */
    public long solution(int n) {
        if (n < 3) return n;

        int[] arr = new int[n + 1];
        arr[1] = 1;
        arr[2] = 2;

        for (int i = 3; i < arr.length; i++) {
            arr[i] = (arr[i - 1] + arr[i - 2]) % 1234567;
        }

        return arr[n];
    }
}