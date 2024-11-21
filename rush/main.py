#!/usr/bin/env python3
from checkmate import *
def main():
    board = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', 'P', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', 'Q', 'K', '.'],]
    king_pos = find_king(board)
    if is_king_under_threat(board, king_pos):
        print("Success")
    else:
        print("Fail")


if __name__ == "__main__":
    main()