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

        # User is asked to select the type of loading condition he or she wishes to apply to the beam
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

                print("\nSTEP 02 : FINDING DEFLECTION AT POINT 'B'")
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
        print("You have selected Propped Cantilever Beam.")

        # Loading conditions menu starts here
        print("\nThe various types of loading conditions available for propped cantilever beam are : ")

        # Point Load for propped cantilever beam
        print("\n1:-> Point Load :- ")
        print("                  |P")
        print("                  |")
        print("                  V")
        print("       |----------------------")
        print("                             O")
        print("       A          B          C")
        print("\n")
        
        # Uniformly Distributed Load for propped cantilever beam
        print("2:-> Uniformly Distributed Load :- ")
        print("                  |W")
        print("                  |")
        print("                  V")
        print("        /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\")
        print("       |----------------------")
        print("                             O")
        print("       A          B          C")
        print("\n")

        # Moment Load for propped cantilever beam
        print("3:-> Moment Load :- ")
        print("                             \\M")
        print("       |----------------------\\")
        print("                             O/")
        print("                             L")
        print("       A          B          C")

        # User is asked to select the type of loading condition he or she wishes to apply to the beam
        load_proppedcantilever = input("Please specify the loading condition (1, 2 or 3) : ")

        # If the loading condition selected is Point Load then the following if statement will be executed
        if load_proppedcantilever == '1':
            print("You have selected Point Load as the loading condition.")

            # User is asked to enter values for load, length of beam, modulus of elasticity and moment of inertia
            P = input("\nEnter load magnitude (P) in N : ")
            L = input("Enter length of beam (L) in mm : ")
            E = input("Enter modulus of elasticity (E) of the material of beam in N/mm^2 : ")
            I = input("Enter moment of inertia (I) of beam in mm^4 : ")
            
            # Menu for various structural analysis methods starts here
            print("\nThe various methods of analysis available are : ")
            print("1:-> Strain Energy Method")
            print("2:-> Minimum Potential Energy Theorem Method")
            print('method3')
            
            # User is asked to select the method of structural analysis
            analysis_proppedcantilever = input("\nPlease select the method of analysis (1, 2 or 3) : ")
            
            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_proppedcantilever == '1':
                print("You have selected Strain Energy Method.")

                # This method is not ready right now.

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")
            
            # If the method of analysis selected is Minimum Energy Theorem Method then the following if statement will be executed
            elif analysis_proppedcantilever == '2':
                print("You have selected Minimum Potentital Energy Theorem Method.")

                print("\nApproach:- We will first find redundant for the two the spans AB and BC and then we will superimpose them to find the redundant for the complete beam. ")
                redundantAB = (float(P)*5)/14
                print("Redundant reaction for span AB = R\' = 5P/14 = " + str(redundantAB) + " N")
                print("Redundant reaction for span BC = R\" = 0 N")
                print("Therefore, total redundant reaction for beam AC = R = R\' + R\" = " + str(redundantAB) + " N")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

            else:
                print('not ready')

        # If the type of loading condition selected is uniformly distributed load then the following elif statement will be executed
        elif load_proppedcantilever == '2':
            print("You have selected Uniformly Distributed Load as the loading condition.")
            
            # User is asked to enter values for uniformly distributed load, length of beam, modulus of elasticity and moment of inertia
            W = input("\nEnter uniformly distributed load (w) in N/mm : ")
            L = input("Enter length of beam (L) in mm : ")
            E = input("Enter modulus of elasticity (E) of the material of beam in N/mm^2 : ")
            I = input("Enter moment of inertia (I) of beam in mm^4 : ")

            # Menu for various structural analysis methods starts here
            print("\nThe various methods of analysis available are : ")
            print("1:-> Strain Energy Method")
            print("2:-> Minimum Potential Energy Theorem Method")
            print('method3')

            # User is asked to select the method of structural analysis
            analysis_propepdcantilever = input("\nPlease select the method of analysis (1, 2 or 3) : ")

            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_proppedcantilever == '1':
                print("You have selected Strain Energy Method.")

                # This method is not ready right now.

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

            # If the method of analysis selected is Minimum Potential Energy Method then the following elif statement will be executed
            elif analysis_proppedcantilever == '2':
                print("You have selected Minimum Potential Energy Method.")

                print("\nApproach:- We will get the true value of redundant reaction when the total strain energy in the beam will be minimum.")
                redundant = (3*int(W)*int(L))/8
                print("Redundant reaction in the beam = R = 3WL/8 = " + str(redundant) + " N")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

            else:
                print('not ready')

        # If the type of loading condition selected is moment load then the following else statement will be executed
        else:
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
        print("                              \\M")
        print("        ---------------------- \\")
        print("        ^                    O /")
        print("        A                    B/")
        print("                             L")
        print("\n")


        # User is asked to select the type of loading condition he or she wishes to apply to the beam
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

                print("\nSTEP 02 : FINDING DEFLECTION AT POINT 'B'")
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

                print("\nSTEP 02 : FINDING DEFLECTION AT POINT 'B'")
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

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")
                
            elif analysis_simplysupported == '2':
                print("not ready")

            else:
                print('not ready')
                
                            
    # If the type of beam selected is fixed beam then the following else statement will be executed    
    else:
        print("You have selected Fixed Beam.")

        # Loading conditions menu starts here
        print("\nThe various types of loading conditions available for fixed beam are : ")

        # Point Load for fixed beam
        print("\n1:-> Point Load :- ")
        print("                  |P")
        print("                  |")
        print("                  V")
        print("       |----------------------|")
        print("       A                      B")
        print("\n")
        
        # Uniformly Distributed Load for cantilever beam
        print("2:-> Uniformly Distributed Load :- ")
        print("                  |W")
        print("                  |")
        print("                  V")
        print("        /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\")
        print("       |----------------------|")
        print("       A                      B")
        print("\n")


        # User is asked to select the type of loading condition he or she wishes to apply to the beam
        load_fixed = input("Please specify the loading condition (1, 2 or 3) : ")

        # If the type of loading condition selected is point load then the following if statement will be executed
        if load_fixed == '1':
            print("You have selected Point Load as the loading condition.")

            # User is asked to enter values for load, length of beam, modulus of elasticity and moment of inertia
            P = input("\nEnter load magnitude (P) in N : ")
            L = input("Enter length of beam (L) in mm : ")
            E = input("Enter modulus of elasticity (E) of the material of beam in N/mm^2 : ")
            I = input("Enter moment of inertia (I) of beam in mm^4 : ")
            
            # Menu for various structural analysis methods starts here
            print("\nThe various methods of analysis available are : ")
            print("1:-> Strain Energy Method")
            print("2:-> Consistent Deformation Method")
            print('method3')
            
            # User is asked to select the method of structural analysis
            analysis_fixed = input("\nPlease select the method of analysis (1, 2 or 3) : ")
            
            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_fixed == '1':
                print("You have selected Strain Energy Method.")
                
                # This method is not ready right now.

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

            # If the method of analysis selected is Consistent Deformation Method then the following elif statement will be executed
            elif analysis_fixed == '2':
                print("You have selected Consistent Deformation Theorem Method.")

                print("\nSTEP 01: CALCULATING DEGREE OF STATIC INDETERMINACY (Ds) ")
                print("Number of actual reactions, R = 4")
                print("Number oe equations available, E = 2")
                print("Degree of Static Indeterminacy, Ds = R - E = 2")

                print("\nSTEP 02: REMOVING REDUNDANT REACTIONS AND CALCULATING DEFLECTIONS DUE TO LOADING")
                print("Let 'Ma' be the redundant reaction at A and 'Mb' be the redundant reaction at B.")
                deltaA1 = (float(P)*float(L)*float(L))/(16*float(E)*float(I))
                deltaB1 = -(float(P)*float(L)*float(L))/(16*float(E)*float(I))
                print("Deflection at A due to loading, Delta(A1) = " + str(deltaA1))
                print("Deflection at B due to loading, Delta(A2) = " + str(deltaB1))

                print("\nSTEP 03: REMOVING LOADING AND CALCULATING DEFLECTIONA DUE TO REDUNDANT REACTIONS")
                print("Let 'Ma' be the redundant reaction at A and 'Mb' be the redundant reaction at B.")
                Ma = (float(P)*float(L))/8
                deltaA2 = -(float(Ma)*float(L))/(3*float(E)*float(I))
                deltaB2 = (float(Ma)*float(L))/(6*float(E)*float(I))
                print("Deflection at A due to redundant reaction at A, Delta(A2) = " + str(deltaA2))
                print("Deflection at B due to redundant reaction at A, Delta(B2) = " + str(deltaB2))
                Mb = (float(P)*float(L))/8
                deltaA3 = -(float(Mb)*float(L))/(6*float(E)*float(I))
                deltaB3 = (float(Mb)*float(L))/(3*float(E)*float(I))
                print("Deflection at A due to redundant reaction at B, Delta(A3) = " + str(deltaA3))
                print("Deflection at B due to redundant reaction at B, Delta(B3) = " + str(deltaB3))

                print("\nSTEP 04: OBTAINING COMPATIBILITY EQUATION AND SOLVING FOR 'Ma' and 'Mb'")
                print("Approach:- To solve for redundant reactions, we need one more equation which can be obtained by compatability. It is quite evident that the deflection at the fixed supports A and B is zero.")
                print("Therefore, deflection at A, Delta(A) = Delta(A1) + Delta(A2) + Delta (A3) = 0")
                print("Also, delfection at B, Delta(B) = Delta(B1) + Delta(B2) + Delta(B3) = 0")
                print("Solving the above two equations, we get redundant reaction at A, Ma = PL/8 = " + str(Ma) + " N")
                print("Redundant reaction at B, Mb = PL/8 = " + str(Mb) + " N")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")


            # If method 3 of analysis is selected
            else:
                print('not ready')

        # If the type of loading condition selected is uniformly distributed load then the following else statement will be executed
        else:
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
            analysis_fixed = input("\nPlease select the method of analysis (1, 2 or 3) : ")

            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_fixed == '1':
                print("You have selected Strain Energy Method.")

                # This method is not ready right now.

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

            elif analysis_fixed == '2':
                print("You have selected Consistent Deformation Theorem Method.")

                print("\nSTEP 01: CALCULATING DEGREE OF STATIC INDETERMINACY (Ds) ")
                print("Number of actual reactions, R = 4")
                print("Number oe equations available, E = 2")
                print("Degree of Static Indeterminacy, Ds = R - E = 2")

                print("\nSTEP 02: REMOVING REDUNDANT REACTIONS AND CALCULATING DEFLECTIONS DUE TO LOADING")
                print("Let 'Ma' be the redundant reaction at A and 'Mb' be the redundant reaction at B.")
                deltaA1 = (float(W)*float(L)*float(L)*float(L))/(24*float(E)*float(I))
                deltaB1 = -(float(W)*float(L)*float(L)*float(L))/(24*float(E)*float(I))
                print("Deflection at A due to loading, Delta(A1) = " + str(deltaA1))
                print("Deflection at B due to loading, Delta(A2) = " + str(deltaB1))

                print("\nSTEP 03: REMOVING LOADING AND CALCULATING DEFLECTIONA DUE TO REDUNDANT REACTIONS")
                print("Let 'Ma' be the redundant reaction at A and 'Mb' be the redundant reaction at B.")
                Ma = (float(W)*float(L)*float(L))/12
                deltaA2 = -(float(Ma)*float(L))/(3*float(E)*float(I))
                deltaB2 = (float(Ma)*float(L))/(6*float(E)*float(I))
                print("Deflection at A due to redundant reaction at A, Delta(A2) = " + str(deltaA2))
                print("Deflection at B due to redundant reaction at A, Delta(B2) = " + str(deltaB2))
                Mb = (float(W)*float(L)*float(L))/8
                deltaA3 = -(float(Mb)*float(L))/(6*float(E)*float(I))
                deltaB3 = (float(Mb)*float(L))/(3*float(E)*float(I))
                print("Deflection at A due to redundant reaction at B, Delta(A3) = " + str(deltaA3))
                print("Deflection at B due to redundant reaction at B, Delta(B3) = " + str(deltaB3))

                print("\nSTEP 04: OBTAINING COMPATIBILITY EQUATION AND SOLVING FOR 'Ma' and 'Mb'")
                print("Approach:- To solve for redundant reactions, we need one more equation which can be obtained by compatability. It is quite evident that the deflection at the fixed supports A and B is zero.")
                print("Therefore, deflection at A, Delta(A) = Delta(A1) + Delta(A2) + Delta (A3) = 0")
                print("Also, delfection at B, Delta(B) = Delta(B1) + Delta(B2) + Delta(B3) = 0")
                print("Solving the above two equations, we get redundant reaction at A, Ma = WL^2/12 = " + str(Ma) + " N")
                print("Redundant reaction at B, Mb = WL^2/12 = " + str(Mb) + " N")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

# If the user doesn't wish to continue with the program for beam analysis then the following else statement will be executed
else:
    print(exit)
    exit()
