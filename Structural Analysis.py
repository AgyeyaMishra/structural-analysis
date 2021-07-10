print("\t\t\t\t\tWELCOME TO THE COMPUTERISED VERSION OF STRUCTURAL ANALYSIS OF BEAMS")
i = 0
while (i < 148):
    print("*", end = '')
    i = i + 1

# Printing the initial instructions for our structural analysis program
print("\n \t Instructions:- \n \t 1:-> Select the type of beam to analyse. \n \t 2:-> Specify the loading conditions. \n \t 3:-> Select the preferred method of analysis. \n \t 4:-> Enter the corresponding values.\n")

j = 0
while (j < 148):
    print("*", end = '')
    j = j + 1

choice = input("\nPlease enter 'y' to begin and 'n' to discontinue : ")
while(choice == 'y'):
    # Beam menu starts here
    print("\nThe various types of beams available are:-")
    print("1:-> Cantilever Beam")
    print("2:-> Propped Cantilever Beam")
    print("3:-> Simply Supported Beam")
    print("4:-> Fixed Beam")

    # User is asked to select the type of beam he or she wishes to analyse
    type_of_beam = input("\nPlease select the type of beam to analyse (1, 2, 3 or 4) : ")


    if type_of_beam =='1':
        print('specify the loading conditions')
        print('1) Point load :           |P')
        print('                          V')
        print('              A|-----------B')
        print('\n \n')
        print('2) UDl        :      W')
        print('              /\\/\\/\\/\\/\\/\\/\\')
        print('             A|-------------B ')
        print('\n \n')
        print('3) Moment     :             \ M')
        print('              A|------------/B')
        print('                           V')
        load01 = input('load type (1/2/3) : ')
        if load01== '1':
            p = input('P : ')
            l = input('length of beam : ')
            E = input('modulus of elasticity : ')
            I = input('moment of inertia : ')
            print()
            print('selecting the method to be used')
            print('1) Strain Energy Method')
            print('method2')
            print('method3')
            print()
            method01 = input('mehthod to be used (1/2/3) : ')
            if method01 == '1':
                print('STEP 01 : CALCULATING STRAIN ENERGY (u)')
                u = (int(p)*int(p)*int(l)*int(l)*int(l))/(3*int(E)*int(I))
                print("strain energy,u = " + str(u))
                print("STEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (int(p)*int(l)*int(l)*int(l))/(3*int(E)*int(I))
                print('deflection = ' + str(deflection))

            elif method01 == '2':
                print("not ready")

            else:
                print('not ready')

        elif load01 =='2':
            w = input('w : ')
            l = input('length of beam : ')
            E = input('modulus of elasticity : ')
            I = input('moment of inertia : ')
            print()
            print('selecting the method to be used')
            print('1) Strain Energy Method')
            print('method2')
            print('method3')
            print()
            method = input('mehthod to be used (1/2/3) : ')
            if method == '1':
                print('STEP 01 : CALCULATING STRAIN ENERGY (u)')
                u = (int(w)*int(w)*int(l)*int(l)*int(l)*int(l))/(8*int(E)*int(I))
                print("strain energy,u = " + str(u))
                print("STEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (5*int(w)*int(l)*int(l)*int(l)*int(l))/(48*int(E)*int(I))
                print('deflection' + str(deflection))

                choice = input("\nEnter 'y' if you wish to continue otherwise enter 'n' : ")

            elif method == '2':
                print("not ready")

            else:
                print('not ready')


        else:
            M = input('M : ')
            l = input('length of beam : ')
            E = input('modulus of elasticity : ')
            I = input('moment of inertia : ')
            print()
            print('selecting the method to be used')
            print('1) Strain Energy Method')
            print('method2')
            print('method3')
            print()
            method = input('mehthod to be used (1/2/3) : ')
            if method == '1':
                print('STEP 01 : CALCULATING STRAIN ENERGY (u)')
                u = (int(M)*int(M)*int(l))/(2*int(E)*int(I))
                print("strain energy,u = " + str(u))
                print("STEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (int(M)*int(l))/(int(E)*int(I))
                print('deflection' + str(deflection))

            elif method == '2':
                print("not ready")

            else:
                print('not ready')

    elif type_of_beam == '2':
        print('not ready')

    elif type_of_beam == '3':
        print('specify the loading conditions')
        print('1) Point load :      |P     ')
        print('                     V')
        print('              A-------------C')
        print('              ^      B      O')
        print('\n \n')
        print('2) UDL       :       W      ')
        print('             /\\/\\/\\/\\/\\/\\/\\/\\')
        print('             A--------------C')
        print('              ^      B      O')
        print('\n \n')
        print('3) Moment    :               \\')
        print('             A---------------/C')
        print('              ^       B     VO')
        load = input('load type (1/2/3) : ')
        if load == '1':
            p = input('P : ')
            l = input('length of beam : ')
            E = input('modulus of elasticity : ')
            I = input('moment of inertia : ')
            print()
            print('selecting the method to be used')
            print('1) Strain Energy Method')
            print('method2')
            print('method3')
            print()
            method = input('mehthod to be used (1/2/3) : ')
            if method == '1':
                print('STEP 01 : CALCULATING STRAIN ENERGY (u)')
                u = (int(p)*int(p)*int(l)*int(l)*int(l))/(96*int(E)*int(I))
                print("strain energy,u = " + str(u))
                print("STEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (int(p)*int(l)*int(l)*int(l))/(48*int(E)*int(I))
                print('deflection' + str(deflection))

            elif method == '2':
                print("not ready")

            else:
                print('not ready')

        elif load == '2':
            w = input('W : ')
            l = input('length of beam : ')
            E = input('modulus of elasticity : ')
            I = input('moment of inertia : ')
            print()
            print('selecting the method to be used')
            print('1) Strain Energy Method')
            print('method2')
            print('method3')
            print()
            method = input('method to be used (1/2/3) : ')
            if method == '1':
                print('STEP 01 : CALCULATING STRAIN ENERGY (u)')
                u = (int(w)*int(w)*int(l)*int(l)*int(l)*int(l)*int(l))/(96*int(E)*int(I))
                print("strain energy,u = " + str(u))
                print("STEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (int(w)*int(l)*int(l)*int(l)*int(l))/(48*int(E)*int(I))
                print('deflection' + str(deflection))

            elif method == '2':
                print("not ready")

            else:
                print('not ready')

        else:
            w = input('W : ')
            l = input('length of beam : ')
            E = input('modulus of elasticity : ')
            I = input('moment of inertia : ')
            print()
            print('selecting the method to be used')
            print('1) Strain Energy Method')
            print('method2')
            print('method3')
            print()
            method = input('method to be used (1/2/3) : ')
            if method == '1':
                print('ERROR : This method does not work for the given conditions')
                
            elif method == '2':
                print("not ready")

            else:
                print('not ready')
                
                            
        
    else:
        print('not ready')

else:
    print(exit)
    exit()
