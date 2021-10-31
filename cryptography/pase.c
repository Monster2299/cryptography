//Mono Alphabebit Substitutional Encription and Decryption.
#include <stdio.h>
#include <string.h>
int main()
{
  	 int i,k,l,j;
   	char str[20];
	printf("Enter a String :");
  	fgets(str, 20, stdin);

printf("what do you want \n1.encod\n2.decode\n");
scanf("%d",&k);
if(k==1){
l=strlen(str);
		for(i=0;i<=l;i++){
			j = str[i];
			printf("%c",j+5);
			
			}
}
if(k==2){
l=strlen(str);
		for(i=0;i<=l;i++){
			j = str[i];
			printf("%c",j-5);
			
			}
}

printf("\n");
   return 0;
}
