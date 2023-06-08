Script that switches the current user to the user betty.
#!/bin/bash
su betty


script that prints the effective username of the current user.
#!/bin/bash
whoami


script that prints all the groups the current user is part of.
#!/bin/bash
groups


script that changes the owner of the file hello to the user betty.
#!/bin/bash
sudo chown betty hello


script that creates an empty file called hello.
#!/bin/bash
touch hello


script that adds execute permission to the owner of the file hello.
#!/bin/bash
chmod u+x hello


script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello
#!/bin/bash
chmod u+x,g+x,o+r hello
