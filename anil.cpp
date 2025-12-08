#include <bits/stdc++.h>
using namespace std;

bool isValid(const vector<vector<int>>& board, int r, int c, int val) {
    for (int i = 0; i < 9; ++i) {
        if (board[r][i] == val) return false;
        if (board[i][c] == val) return false;
        int br = 3*(r/3) + i/3;
        int bc = 3*(c/3) + i%3;
        if (board[br][bc] == val) return false;
    }
    return true;
}

bool solveSudoku(vector<vector<int>>& board) {
    for (int r = 0; r < 9; ++r) {
        for (int c = 0; c < 9; ++c) {
            if (board[r][c] == 0) {
                for (int val = 1; val <= 9; ++val) {
                    if (isValid(board, r, c, val)) {
                        board[r][c] = val;
                        if (solveSudoku(board)) return true;
                        board[r][c] = 0;
                    }
                }
                return false;
            }
        }
    }
    return true;
}

void printBoard(const vector<vector<int>>& board) {
    for (int r = 0; r < 9; ++r) {
        for (int c = 0; c < 9; ++c) {
            cout << board[r][c] << (c==8 ? "" : " ");
        }
        cout << '\n';
    }
}

int main() {
    vector<vector<int>> board(9, vector<int>(9, 0));
    // Read 9 lines of 9 integers (use 0 for empty cells).
    // Example input line: 5 3 0 0 7 0 0 0 0
    for (int r = 0; r < 9; ++r) {
        for (int c = 0; c < 9; ++c) {
            if (!(cin >> board[r][c])) {
                cerr << "Expected 81 integers (use 0 for blanks).\n";
                return 1;
            }
        }
    }

    if (solveSudoku(board)) {
        printBoard(board);
        return 0;
    } else {
        cout << "No solution exists\n";
        return 1;
    }
}
// ...existing code...