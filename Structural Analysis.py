print("\t\t\t\t\tWELCOME TO THE COMPUTERISED VERSION OF STRUCTURAL ANALYSIS OF BEAMS")
i = 0
while (i < 148):
    print("*", end = '')
    i = i + 1

# Printing the initial instructions for our structural analysis program
print("\n \t Instructions:- \n \t 1:-> Select the type of beam to analyse. \n \t 2:-> Specify the loading condition. \n \t 3:-> Select the preferred method of analysis. \n \t 4:-> Enter the corresponding values.\n")

j = 0
while (j < 148):
    print("*", end = '')
    j = j + 1

# User is asked whether he or she wishes to begin the beam analysis program or not
choice = input("\nPlease enter 'y' to begin and 'n' to discontinue : ")

# If the user wishes to begin the program for beam analysis then the following while loop will be executed
while(choice == 'y'):
    # Beam menu starts here
    print("\nThe various types of beams available are:-")
    print("1:-> Cantilever Beam")
    print("2:-> Propped Cantilever Beam")
    print("3:-> Simply Supported Beam")
    print("4:-> Fixed Beam")

    # User is asked to select the type of beam he or she wishes to analyse
    type_of_beam = input("\nPlease select the type of beam to analyse (1, 2, 3 or 4) : ")


    # If the type of beam select is cantilever beam then the following if statement will be executed
    if type_of_beam =='1':
        print("You have selected Cantilever Beam.")

        # Loading conditions menu starts here
        print("\nThe various types of loading conditions available for cantilever beam are : ")

        # Point Load for cantilever beam
        print("\n1:-> Point Load :- ")
        print("                             |P")
        print("                             |")
        print("                             V")
        print("       |----------------------")
        print("       A                     B")
        print("\n")
        
        # Uniformly Distributed Load for cantilever beam
        print("2:-> Uniformly Distributed Load :- ")
        print("                  |W")
        print("                  |")
        print("                  V")
        print("        /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\")
        print("       |----------------------")
        print("       A                     B")
        print("\n")

        # Moment Load for cantilever beam
        print("3:-> Moment Load :- ")
        print("                             \\M")
        print("       |----------------------\\")
        print("       A                     B/")
        print("                             L")

        # User is asked to select the type of loading condition her or she wishes to apply to the beam
        load_cantilever = input("Please specify the loading condition (1, 2 or 3) : ")

        # If the type of loading condition selected is point load then the following if statement will be executed
        if load_cantilever == '1':
            print("You have selected Point Load as the loading condition.")

            # User is asked to enter values for load, length of beam, modulus of elasticity and moment of inertia
            P = input("\nEnter load magnitude (P) in N : ")
            L = input("Enter length of beam (L) in mm : ")
            E = input("Enter modulus of elasticity (E) of the material of beam in N/mm^2 : ")
            I = input("Enter moment of inertia (I) of beam in mm^4 : ")
            
            # Menu for various structural analysis methods starts here
            print("\nThe various methods of analysis available are : ")
            print("1:-> Strain Energy Method")
            print('method2')
            print('method3')
            
            # User is asked to select the method of structural analysis
            analysis_cantilever = input("\nPlease select the method of analysis (1, 2 or 3) : ")
            
            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_cantilever == '1':
                print("You have selected Strain Energy Method.")

                print("\nSTEP 01 : CALCULATING STRAIN ENERGY (u)")
                u = (float(P)*float(P)*float(L)*float(L)*float(L))/(6*float(E)*float(I))
                print("Strain energy in this case, represented by u, is given as = " + str(u) + " N-mm")

                print("\nSTEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (float(P)*float(L)*float(L)*float(L))/(3*float(E)*float(I))
                print("Deflection at point 'B' is given as  = " + str(deflection) + " mm ")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")



            elif analysis_cantilever == '2':
                print("not ready")

            else:
                print('not ready')

        # If the type of loading condition selected is uniformly distributed load then the following elif statement will be executed
        elif load_cantilever == '2':
            print("You have selected Uniformly Distributed Load as the loading condition.")
            
            # User is asked to enter values for uniformly distributed load, length of beam, modulus of elasticity and moment of inertia
            W = input("\nEnter uniformly distributed load (w) in N/mm : ")
            L = input("Enter length of beam (L) in mm : ")
            E = input("Enter modulus of elasticity (E) of the material of beam in N/mm^2 : ")
            I = input("Enter moment of inertia (I) of beam in mm^4 : ")

            # Menu for various structural analysis methods starts here
            print("\nThe various methods of analysis available are : ")
            print("1:-> Strain Energy Method")
            print('method2')
            print('method3')

            # User is asked to select the method of structural analysis
            analysis_cantilever = input("\nPlease select the method of analysis (1, 2 or 3) : ")

            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_cantilever == '1':
                print("You have selected Strain Energy Method.")

                print('\nSTEP 01 : CALCULATING STRAIN ENERGY (u)')
                u = (float(W)*float(W)*float(L)*float(L)*float(L)*float(L))/(8*float(E)*float(I))
                print("Strain energy in this case, represented by u, is given as = " + str(u) + " N-mm")

                print("\nSTEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (5*float(W)*float(L)*float(L)*float(L)*float(L))/(48*float(E)*float(I))
                print("Deflection at point 'B' is given as  = " + str(deflection) + " mm ")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

            elif analysis_cantilever == '2':
                print("not ready")

            else:
                print('not ready')


        # If the type of loading condition selected is moment load then the following else statement will be executed
        else:
            print("You have selected Moment Load as the loading condition.")
            
            # User is asked to enter values for moment load, length of beam, modulus of elasticity and moment of inertia
            M = input("\nEnter moment load (M) in N-mm : ")
            L = input("Enter length of beam (L) in mm : ")
            E = input("Enter modulus of elasticity (E) of the material of beam in N/mm^2 : ")
            I = input("Enter moment of inertia (I) of the beam in mm^4  : ")
            
             # Menu for various structural analysis methods starts here
            print("\nThe various methods of analysis available are : ")
            print("1:-> Strain Energy Method")
            print('method2')
            print('method3')

            # User is asked to select the method of structural analysis
            analysis_cantilever = input("\nPlease select the method of analysis (1, 2 or 3) : ")


            if analysis_cantilever == '1':
                print("You have selected Strain Energy Method.")

                print("\nSTEP 01 : CALCULATING STRAIN ENERGY (u)")
                u = (float(M)*float(M)*float(L))/(2*float(E)*float(I))
                print("Strain energy in this case, represented by u, is given as = " + str(u) + " N-mm")

                print("STEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (float(M)*float(L))/(float(E)*float(I))
                print("Deflection at point 'B' is given as  = " + str(deflection) + " mm ")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

            elif analysis_cantilever == '2':
                print("not ready")

            else:
                print('not ready')

    # If the type of beam selected is propped cantilever beam then the following if statement will be executed
    elif type_of_beam == '2':
        print('not ready')

    # If the type of beam selected is simply supported beam then the following if statement will be executed
    elif type_of_beam == '3':
        print("You have selected Simply Supported Beam.")

        # Loading conditions menu starts here
        print("\nThe various types of loading conditions available for Simply Supported beam are : ")

        # Point Load for Simply Supported beam
        print("\n1:-> Point Load :- ")
        print("                  |P")
        print("                  |")
        print("                  V")
        print("        ----------------------")
        print("        ^         B          O")
        print("        A                    C")
        print("\n")

        # Uniformly Distributed Load for Simply Supported beam
        print("2:-> Uniformly Distrbuted Load :- ")
        print("                  |W")
        print("                  |")
        print("                  V")
        print("        /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\")
        print("        ----------------------")
        print("        ^                    O")
        print("        A                    B")
        print("\n")


        # Moment Load for Simply Supported Beam
        print("3:-> Moment Load :- ")
        print("                             \\M")
        print("       ---------------------- \\")
        print("       ^                    O /")
        print("       A                    B/")
        print("                            L")
        print("\n")


        # User is asked to select the type of loading condition her or she wishes to apply to the beam
        load_simplysupported = input("Please specify the loading condition (1, 2 or 3) : ")

        # If the type of loading condition selected is point load then the following if statement will be executed 
        if load_simplysupported == '1':
            print("You have selected Point Load as the loading condition.")

            # User is asked to enter values for load, length of beam, modulus of elasticity and moment of inertia
            P = input("\nEnter load magnitude (P) in N : ")
            L = input("Enter length of beam (L) in mm : ")
            E = input("Enter modulus of elasticity (E) of the material of beam in N/mm^2 : ")
            I = input("Enter moment of inertia (I) of beam in mm^4 : ")
            
            # Menu for various structural analysis methods starts here
            print("\nThe various methods of analysis available are : ")
            print("1:-> Strain Energy Method")
            print('method2')
            print('method3')
            
            # User is asked to select the method of structural analysis
            analysis_simplysupported = input("\nPlease select the method of analysis (1, 2 or 3) : ")
            
            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_simplysupported == '1':
                print("You have selected Strain Energy Method.")

                print("\nSTEP 01 : CALCULATING STRAIN ENERGY (u)")
                u = (float(P)*float(P)*float(L)*float(L)*float(L))/(96*float(E)*float(I))
                print("Strain energy in this case, represented by u, is given as = " + str(u) + " N-mm")

                print("STEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (float(P)*float(L)*float(L)*float(L))/(48*float(E)*float(I))
                print("Deflection at point 'B' is given as  = " + str(deflection) + " mm ")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

            elif analysis_simplysupported == '2':
                print("not ready")

            else:
                print('not ready')

        # If the type of loading condition selected is uniformly distributed load then the following elif statement will be executed
        elif load_simplysupported == '2':
            print("You have selected Uniformly Distributed Load as the loading condition.")
            
            # User is asked to enter values for uniformly distributed load, length of beam, modulus of elasticity and moment of inertia
            W = input("\nEnter uniformly distributed load (w) in N/mm : ")
            L = input("Enter length of beam (L) in mm : ")
            E = input("Enter modulus of elasticity (E) of the material of beam in N/mm^2 : ")
            I = input("Enter moment of inertia (I) of beam in mm^4 : ")

            # Menu for various structural analysis methods starts here
            print("\nThe various methods of analysis available are : ")
            print("1:-> Strain Energy Method")
            print('method2')
            print('method3')

            # User is asked to select the method of structural analysis
            analysis_simplysupported = input("\nPlease select the method of analysis (1, 2 or 3) : ")

            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_simplysupported == '1':
                print("You have selected Strain Energy Method.")

                print("\nSTEP 01 : CALCULATING STRAIN ENERGY (u)")
                u = (float(W)*float(W)*float(L)*float(L)*float(L)*float(L)*float(L))/(96*float(E)*float(I))
                print("Strain energy in this case, represented by u, is given as = " + str(u) + " N-mm")

                print("STEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (float(W)*float(L)*float(L)*float(L)*float(L))/(48*float(E)*float(I))
                print("Deflection at point 'B' is given as  = " + str(deflection) + " mm ")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

            elif analysis_simplysupported == '2':
                print("not ready")

            else:
                print('not ready')

        # If the type of loading condition selected is moment load then the following else statement will be executed
        else:
            print("You have selected Moment Load as the loading condition.")
            
            # User is asked to enter values for moment load, length of beam, modulus of elasticity and moment of inertia
            M = input("\nEnter moment load (M) in N-mm : ")
            L = input("Enter length of beam (L) in mm : ")
            E = input("Enter modulus of elasticity (E) of the material of beam in N/mm^2 : ")
            I = input("Enter moment of inertia (I) of the beam in mm^4  : ")
            
             # Menu for various structural analysis methods starts here
            print("\nThe various methods of analysis available are : ")
            print("1:-> Strain Energy Method")
            print('method2')
            print('method3')

            # User is asked to select the method of structural analysis
            analysis_simplysupported = input("\nPlease select the method of analysis (1, 2 or 3) : ")

            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_simplysupported == '1':
                print("You have selected Strain Energy Method.")

                print("\nERROR : This method does not work for the given loading condition.")
                
            elif analysis_simplysupported == '2':
                print("not ready")

            else:
                print('not ready')
                
                            
        
    else:
        print('not ready')

# If the user doesn't wish to continue with the program for beam analysis then the following else statement will be executed
else:
    print(exit)
    exit()
