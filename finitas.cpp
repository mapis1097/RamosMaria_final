#include <iostream>
#include<cmath>
//se llama el metodo
void ecuacion (float s, float d, float Ctiempo, float Cespacio, float deltaT, float deltaX);

//ejecuta el codigo
int main (){
    //variables
    float deltaX = 0.01;
    float deltaT = 0.01;
    float tiempo = 1;
    float D = 1;
    float s = 1;
    float inicial = exp(-0.5*((deltaX-1)*(deltaX-1)/((0.25)*(0.25))));
    float CTiempo = 0.5;
    float CEspacio = 2.0;
    ecuacion(s, D, CTiempo, CEspacio, deltaT, deltaX);
   
 return 0;
}




//metodos
void ecuacion (float s, float d, float Ctiempo, float Cespacio, float deltaT, float deltaX){
    float anterior[30];
    float actual[30];
  for (int k = 0; k < Cespacio; k++){
            std::cout << anterior[k]<< "\t";
        }
        std::cout<<std::endl;
        for (int j = 0; j < Cespacio; j ++)
        {
            if (j == 0 || j == Cespacio-1){
                actual[j] = 0;
            }
            else{
                actual [j] = anterior[j] + (d*deltaT/pow(deltaX,2))*(anterior[j+1]- (2.0* anterior[j]) + anterior[j-1]) + (deltaT*s);        
            }
           
        }
        for ( int l = 0; l < Cespacio; l++){
            anterior[l] = actual[l];
        }
         
    }
