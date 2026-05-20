#!/bin/bash

echo "Enter commit message:"
read commit_msg

git add .
git commit -m "$commit_msg"
git push git@github-account1:daniaalkhmous99/Final-Project.git main

echo " Code pushed successfully!"