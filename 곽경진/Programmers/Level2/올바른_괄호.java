/*
프로그래머스 올바른_괄호
https://school.programmers.co.kr/learn/courses/30/lessons/12909

    스택 활용 문제 풀이 
*/

import java.util.Stack;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }

        return stack.isEmpty();
    }
}