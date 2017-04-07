#!/bin/bash

if [ -z "$1" ]; then
  echo "missing current city"
  exit 1
fi
CURR="$1"

if [ -z "$2" ]; then
  echo "missing next city"
  exit 1
fi
NEXT="$2"

svn cp $CURR $NEXT

sed -i "s/$CURR/$NEXT/g" "$NEXT"/*

echo "New requirements profile '$NEXT' created locally."
echo "Review 'svn diff' output and then commit."
svn diff
