# UsabilityEvaluation
This is the repository to help us collaborate and maintain version control.

## Important instructions:
1. Go through the following videos to learn about github and its uses.
https://www.youtube.com/watch?v=0fKg7e37bQE
https://www.youtube.com/watch?v=oFYyTZwMyAg
2. This is the master branch that we shall use.
3. This is what you have to do:
* Fork this repository by pressing the fork button on top.
* Then, go to your profile, find the forked repository (it has the same name as the original repository).
* Now, press the Clone or download button and copy the URL. Then clone it into a folder by doing:

      git clone <URL>
* Create a branch, name it as "development" branch.
      
      git checkout -b development
* Then, do whatever changes you've to do. Check your changes by doing this command, it shows what files you made changes into.
      
      git status
* [OPTIONAL] If you do see a file you changed but forgot what exactly you changed, you can refer to that by doing:
     
      git diff
* Once you're done with changes and feel good enough to push the code, do these inside the cloned folder:
      
      git add .
      git commit -m "Put meaningful message here"
      git push origin master
* Then, once the code is reviewed and approved, you can issue a Pull request by doing the following:
    
      Go to your forked repository.
      Press Pull Request button on top.
      Put a meaningful message, changes done and issue the request.
      Upon resolving conflicts, the code will be merged.

## How to update your master branch?
1. When you forked from my repository, you had the version of my repository at that date and time.

2. Overtime there's some changes from various members which cause changes into my master branch.

3. These changes won't be directly reflected into your master branch. To get these changes, here's what you've to do:

  1. git remote add upstream https://github.com/ShubhangiSk/UsabilityEvaluation.git
  2. git fetch upstream
  3. git checkout master
  4. git rebase upstream/master 4.1. IF you see some "Auto-merging, CONFLICT", it means there's been some merge-conflict. If this           happens, leave it then and there (unless you know to handle merge-conflicts).
  5. git push -f origin master
Note how the step 5 pushes into origin and not upstream. This is because, when you forked and cloned the same into your desktop, the origin points to your forked repo and by step 1, upstream points to the original repository.

## NOTE
Do not push directly to master branch. I.e., do NOT do : git push upstream master.
