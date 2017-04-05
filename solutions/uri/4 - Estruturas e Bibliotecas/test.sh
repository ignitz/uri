#!/bin/bash

function test() {
  g++ $1.cpp -std=c++11 -o $1.out
  if [[ -f $1.out ]]; then
    ./$1.out < input.txt
    rm -rf $1.out
  else
    echo "Error in compile pass"
  fi
}

test 1522
