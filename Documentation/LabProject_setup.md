# **Social and Assistive Robotics Project setup 1**

The objectives of this section are:
- Setup the project in student's github
- Review the needed tools
- Update and syncronize the repository project

## **1. Setup the project in student's github**

When working in Laboratory groups, we suggest you:
- One student plays the role of `Director`. This student makes a "Fork" of the Professor's github project.
- The `Director` accept the other students as `Collaborators`

- Then the `Collaborators` will make a "fork" of the `Director`'s github project.
- The `Collaborators` will be able to update the github `Director`'s project and participate on the project generation

- Create in your Laptop a local desired Project/Activity folder. Open VScode in that folder.
- First time, clone your forked `Director`'s github project. In `Git bash` VScode terminal, type:
  ```shell
  git clone https://github.com/director_username/Project_Assistive_Robotics
  ```
  >Successives times you can update the project with:
  ```shell
  cd Project_Assistive_Robotics
  git pull
  ```
- First time, open a "Git bash" terminal and configure git with your credentials:
    ```git
    git config --global user.name "your_name"
    git config --global user.email "your_email@alumnes.ub.edu"
    ```

## **2. Update and syncronize the repository project**

When working on a Laboratory project, the objective at the end of a Lab session is to update the changes you have made. 

- To add your contributions to the project, you will proceed:
    ````shell
    cd Project_Assistive_Robotics
    git add .
    git commit -m "your_commit_message"
    git push
    ````
- You will have to enter your PAT
- The `Director` repository is updated with the collaborator's contributions
