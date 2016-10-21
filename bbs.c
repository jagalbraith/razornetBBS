#include <stdio.h>
#include <string.h>

int main ()
{
   char command[50];

   strcpy( command, "/bbs/bbs.py" );
   system(command);

   return(0);
} 
