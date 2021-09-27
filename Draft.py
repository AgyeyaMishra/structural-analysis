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
    print("\nThe various types of beams available under Force method of analysis are:-")
    print("1:-> Cantilever Beam")
    print("2:-> Propped Cantilever Beam")
    print("3:-> Simply Supported Beam")
    print("4:-> Fixed Beam")

    # User is asked to select the type of beam he or she wishes to analyse
    type_of_beam = input("\nPlease select the type of beam to analyse (1, 2, 3 or 4) : ")


    # If the type of beam selected is cantilever beam then the following if statement will be executed
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
                
            # User is asked to select the method of structural analysis
            analysis_cantilever = input("\nPlease select the method of analysis : ")
                
            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_cantilever == '1':
                print("You have selected Strain Energy Method.")

                print("\nSTEP 01 : CALCULATING STRAIN ENERGY (u)")
                u = (float(P)*float(P)*float(L)*float(L)*float(L))/(6*float(E)*float(I))
                print("Strain energy in this case, represented by u, is given as = (P^2*L^3)/(6*E*I) = " + str(u*0.001) + " N-m")

                print("\nSTEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (float(P)*float(L)*float(L)*float(L))/(3*float(E)*float(I))
                print("Deflection at point 'B' is given as = (PL^3)/(3*E*I) = " + str(deflection*0.001) + " m")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

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
            
            # User is asked to select the method of structural analysis
            analysis_cantilever = input("\nPlease select the method of analysis : ")

            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_cantilever == '1':
                print("You have selected Strain Energy Method.")

                print('\nSTEP 01 : CALCULATING STRAIN ENERGY (u)')
                u = (float(W)*float(W)*float(L)*float(L)*float(L)*float(L))/(8*float(E)*float(I))
                print("Strain energy in this case, represented by u, is given as = (W^2*L^4)/(8*E*I) = " + str(u*0.001) + " N-m")

                print("\nSTEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (5*float(W)*float(L)*float(L)*float(L)*float(L))/(48*float(E)*float(I))
                print("Deflection at point 'B' is given as = (5*W*L^4)/(48*E*I) = " + str(deflection*0.001) + " m")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

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

                # User is asked to select the method of structural analysis
                analysis_cantilever = input("\nPlease select the method of analysis : ")

                if analysis_cantilever == '1':
                    print("You have selected Strain Energy Method.")

                    print("\nSTEP 01 : CALCULATING STRAIN ENERGY (u)")
                    u = (float(M)*float(M)*float(L))/(2*float(E)*float(I))
                    print("Strain energy in this case, represented by u, is given as = (M^2*L)/(2*E*I) = " + str(u*0.001) + " N-m")

                    print("\nSTEP 02 : FINDING DEFLECTION AT POINT 'B'")
                    deflection = (float(M)*float(L))/(float(E)*float(I))
                    print("Deflection at point 'B' is given as = (M*L)/(E*I) = " + str(deflection*0.001) + " m")

                    # User is asked whether he or she wishes to continue the analysis or not
                    choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")


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
            print("1:-> Minimum Potential Energy Theorem Method")
            print("2:-> Consistent Deformation Theorem Method")
            
            # User is asked to select the method of structural analysis
            analysis_proppedcantilever = input("\nPlease select the method of analysis (1 or 2) : ")
            
            # If the method of analysis selected is Minimum Energy Theorem Method then the following elif statement will be executed
            if analysis_proppedcantilever == '1':
                print("You have selected Minimum Potentital Energy Theorem Method.")

                print("\nApproach:- We will first find redundant for the two the spans AB and BC and then we will superimpose them to find the redundant for the complete beam. ")
                redundantAB = (float(P)*5)/14
                print("Redundant reaction for span AB = R\' = (5*P)/14 = " + str(redundantAB) + " N")
                print("Redundant reaction for span BC = R\" = 0 N")
                print("Therefore, total redundant reaction for beam AC = R = R\' + R\" = (5*P)/14 = " + str(redundantAB) + " N")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

            # If the method of analysis selected is Consistent Deformation Theorem Method then the following elif statement will be executed     
            elif analysis_proppedcantilever == '2':
                print("You have selected Consistent Deformation Theorem Method.")

                print("\nSTEP 01: CALCULATING DEGREE OF STATIC INDETERMINACY (Ds) ")
                print("Number of actual reactions, R = 3")
                print("Number of equations available, E = 2")
                print("Degree of Static Indeterminacy, Ds = R - E = 1")

                print("\nSTEP 02: REMOVING REDUNDANT REACTIONS AND CALCULATING DISPLACEMENT DUE TO LOADING")
                print("Let 'Rb' be the redundant reaction at B.")
                deltaB1 = -(5*float(P)*float(L)*float(L)*float(L))/(48*float(E)*float(I))
                print("Displacement at B due to applied loading, Delta(B1) = -(5*P*L^3)/(48*E*I) = " + str(deltaB1*0.001) + " m (Taking clockwise direction as negative)")

                print("\nSTEP 03: REMOVING LOADING AND CALCULATING DISPLACEMENT DUE TO REDUNDANT REACTIONS")
                Rb = (5*float(P)/16)
                deltaB2 = (float(Rb)*float(L)*float(L)*float(L))/(3*float(E)*float(I))
                print("Displacement at B due to redundant reaction at B, Delta(B2) = (Rb*L^3)/(3*E*I) = " + str(deltaB2*0.001) + " m")
                
                print("\nSTEP 04: OBTAINING COMPATIBILITY EQUATION AND SOLVING FOR 'Ma' and 'Mb'")
                print("Approach:- To solve for redundant reaction, we need one more equation which can be obtained by compatability. It is quite evident that the displacement at B is zero.")
                print("Total Displacement at B, Delta(B) = Delta(B1) + Delta(B2) = 0")
                print("Substituting the values and solving the above equation, we get redundant reaction at B, Rb = (5*P)/16 = " + str(Rb) + " N")
                Ra = (11*float(P))/16
                Ma = -(3*float(P)*float(L)*float(L))/16
                print("Using the value of redundant reaction at B 'Rb', we can also calculate the following:")
                print("Reaction at A, 'Ra' = P - Rb = P - (5*P)/16 = (11*P)/16 = " + str(Ra) + " N")
                print("Bending Moment at A, 'Ma' = Rb - (P*L/2) = -(3*P*L^2)/16 = " + str(Ma*0.001) + " N-m (Taking clockwise direction as negative)")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")


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
            print("1:-> Minimum Potential Energy Theorem Method")
            print("2:-> Consistent Deformation Theorem Method")

            # User is asked to select the method of structural analysis
            analysis_proppedcantilever = input("\nPlease select the method of analysis (1 or 2) : ")

            # If the method of analysis selected is Minimum Potential Energy Method then the following elif statement will be executed
            if analysis_proppedcantilever == '1':
                print("You have selected Minimum Potential Energy Method.")

                print("\nApproach:- We will get the true value of redundant reaction when the total strain energy in the beam will be minimum.")
                redundant = (3*int(W)*int(L))/8
                print("Redundant reaction in the beam = R = (3*W*L)/8 = " + str(redundant) + " N")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

            # If the method of analysis selected is Consistent Deformation Theorem Method then the following elif statement will be executed
            elif analysis_proppedcantilever == '2':
                print("You have selected Consistent Deformation Theorem Method.")

                print("\nSTEP 01: CALCULATING DEGREE OF STATIC INDETERMINACY (Ds) ")
                print("Number of actual reactions, R = 3")
                print("Number of equations available, E = 2")
                print("Degree of Static Indeterminacy, Ds = R - E = 1")

                print("\nSTEP 02: REMOVING REDUNDANT REACTIONS AND CALCULATING DISPLACEMENT DUE TO LOADING")
                print("Let 'Rb' be the redundant reaction at B.")
                deltaB1 = -(float(W)*float(L)*float(L)*float(L)*float(L))/(8*float(E)*float(I))
                print("Displacement at B due to applied loading, Delta(B1) = -(W*L^4)/(8*E*I) = " + str(deltaB1*0.001) + " m (Taking clockwise direction as negative)")

                print("\nSTEP 03: REMOVING LOADING AND CALCULATING DISPLACEMENT DUE TO REDUNDANT REACTIONS")
                Rb = (3*float(W)*float(L))/8
                deltaB2 = (float(Rb)*float(L)*float(L)*float(L))/(3*float(E)*float(I))
                print("Displacement at B due to redundant reaction at B, Delta(B2) = (Rb*L^3)/(3*E*I) = " + str(deltaB2*0.001) + " m")
                
                print("\nSTEP 04: OBTAINING COMPATIBILITY EQUATION AND SOLVING FOR 'Ma' and 'Mb'")
                print("Approach:- To solve for redundant reaction, we need one more equation which can be obtained by compatability. It is quite evident that the displacement at B is zero.")
                print("Total displacement at B, Delta(B) = Delta(B1) + Delta(B2) = 0")
                print("Substituting the values and solving the above equation, we get redundant reaction at B, Rb = (3*W*L)/8 = " + str(Rb) + " N")
                Ra = (5*float(W)*float(L))/8
                Ma = -(float(W)*float(L)*float(L))/8
                print("Using the value of redundant reaction at B 'Rb', we can also calculate the following:")
                print("Reaction at A, 'Ra' = W*L - Rb = W*L - (3*W*L)/8 = (5*W*L)/8 = " + str(Ra) + " N")
                print("Bending Moment at A, 'Ma' = Rb - WL^2/2 = -(W*L^2)/8 = " + str(Ma*0.001) + " N-m (Taking clockwise direction as negative)")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

        # If the type of loading condition selected is moment load then the following else statement will be executed
        else:
            print("ERROR! Not ready.")

            # User is asked whether he or she wishes to continue the analysis or not
            choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")



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
            
            # User is asked to select the method of structural analysis
            analysis_simplysupported = input("\nPlease select the method of analysis : ")
            
            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_simplysupported == '1':
                print("You have selected Strain Energy Method.")

                print("\nSTEP 01 : CALCULATING STRAIN ENERGY (u)")
                u = (float(P)*float(P)*float(L)*float(L)*float(L))/(96*float(E)*float(I))
                print("Strain energy in this case, represented by u, is given as = (P^2*L^3)/(96*E*I) = " + str(u*0.001) + " N-m")

                print("\nSTEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (float(P)*float(L)*float(L)*float(L))/(48*float(E)*float(I))
                print("Deflection at point 'B' is given as = (P*L^3)/(48*E*I) = " + str(deflection*0.001) + " m")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

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

            # User is asked to select the method of structural analysis
            analysis_simplysupported = input("\nPlease select the method of analysis : ")

            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_simplysupported == '1':
                print("You have selected Strain Energy Method.")

                print("\nSTEP 01 : CALCULATING STRAIN ENERGY (u)")
                u = (float(W)*float(W)*float(L)*float(L)*float(L)*float(L)*float(L))/(96*float(E)*float(I))
                print("Strain energy in this case, represented by u, is given as = (W^2*L^5)/(96*E*I) = " + str(u*0.001) + " N-m")

                print("\nSTEP 02 : FINDING DEFLECTION AT POINT 'B'")
                deflection = (float(W)*float(L)*float(L)*float(L)*float(L))/(48*float(E)*float(I))
                print("Deflection at point 'B' is given as = (W*L^$)/(48*E*I) = " + str(deflection*0.001) + " m")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

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

            # User is asked to select the method of structural analysis
            analysis_simplysupported = input("\nPlease select the method of analysis (1, 2 or 3) : ")

            # If the method of analysis selected is Strain Energy Method then the following if statement will be executed
            if analysis_simplysupported == '1':
                print("You have selected Strain Energy Method.")

                print("\nERROR : This method does not work for the given loading condition.")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")
                                
                            
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
            print("1:-> Consistent Deformation Method")
            
            # User is asked to select the method of structural analysis
            analysis_fixed = input("\nPlease select the method of analysis : ")

            # If the method of analysis selected is Consistent Deformation Method then the following elif statement will be executed
            if analysis_fixed == '1':
                print("You have selected Consistent Deformation Theorem Method.")

                print("\nSTEP 01: CALCULATING DEGREE OF STATIC INDETERMINACY (Ds) ")
                print("Number of actual reactions, R = 4")
                print("Number of equations available, E = 2")
                print("Degree of Static Indeterminacy, Ds = R - E = 2")

                print("\nSTEP 02: REMOVING REDUNDANT REACTIONS AND CALCULATING DISPLACEMENTS DUE TO LOADING")
                print("Let 'Ma' be the redundant reaction at A and 'Mb' be the redundant reaction at B.")
                thetaA1 = (float(P)*float(L)*float(L))/(16*float(E)*float(I))
                thetaB1 = -(float(P)*float(L)*float(L))/(16*float(E)*float(I))
                print("Displacement at A due to applied loading, Theta(A1) = (P*L^2)/(16*E*I) = " + str(thetaA1))
                print("Displacement at B due to applied loading, Theta(B1) = -(P*L^2)/(16*E*I) = " + str(thetaB1) + " (Taking clockwise direction as negative)")

                print("\nSTEP 03: REMOVING LOADING AND CALCULATING DISPLACEMENTS DUE TO REDUNDANT REACTIONS")
                print("Let 'Ma' be the redundant reaction at A and 'Mb' be the redundant reaction at B.")
                Ma = (float(P)*float(L))/8
                thetaA2 = -(float(Ma)*float(L))/(3*float(E)*float(I))
                thetaB2 = (float(Ma)*float(L))/(6*float(E)*float(I))
                print("Displacement at A due to redundant reaction at A, Theta(A2) = -(Ma*L)/(3*E*I) = " + str(thetaA2) + " (Taking clockwise direction as negative)")
                print("Displacement at B due to redundant reaction at A, Theta(B2) = (Ma*L)/(6*E*I) = " + str(thetaB2))
                Mb = (float(P)*float(L))/8
                thetaA3 = -(float(Mb)*float(L))/(6*float(E)*float(I))
                thetaB3 = (float(Mb)*float(L))/(3*float(E)*float(I))
                print("\nDisplacement at A due to redundant reaction at B, Theta(A3) = -(Mb*L)/(6*E*I) = " + str(thetaA3) + " (Taking clockwise direction as negative)")
                print("Displacement at B due to redundant reaction at B, Theta(B3) = (Mb*L)/(3*E*I) = " + str(thetaB3))

                print("\nSTEP 04: OBTAINING COMPATIBILITY EQUATION AND SOLVING FOR 'Ma' and 'Mb'")
                print("Approach:- To solve for redundant reactions, we need one more equation which can be obtained by compatability. It is quite evident that the displacement at the fixed supports A and B is zero.")
                print("Therefore, total displacement at A, Theta(A) = Theta(A1) + Theta(A2) + Theta(A3) = 0")
                print("Also, total displacement at B, Theta(B) = Theta(B1) + Theta(B2) + Theta(B3) = 0")
                print("Solving the above two equations, we get redundant reaction at A, Ma = (P*L)/8 = " + str(Ma) + " N")
                print("Redundant reaction at B, Mb = (P*L)/8 = " + str(Mb) + " N")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")


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
            print("1:-> Consistent Deformation Theorem Method")

            # User is asked to select the method of structural analysis
            analysis_fixed = input("\nPlease select the method of analysis : ")

            # If the method of analysis selected is Consistent Deformation Theorem Method then the following elif statement will be executed
            if analysis_fixed == '1':
                print("You have selected Consistent Deformation Theorem Method.")

                print("\nSTEP 01: CALCULATING DEGREE OF STATIC INDETERMINACY (Ds) ")
                print("Number of actual reactions, R = 4")
                print("Number oe equations available, E = 2")
                print("Degree of Static Indeterminacy, Ds = R - E = 2")

                print("\nSTEP 02: REMOVING REDUNDANT REACTIONS AND CALCULATING DISPLACEMENTS DUE TO LOADING")
                print("Let 'Ma' be the redundant reaction at A and 'Mb' be the redundant reaction at B.")
                thetaA1 = (float(W)*float(L)*float(L)*float(L))/(24*float(E)*float(I))
                thetaB1 = -(float(W)*float(L)*float(L)*float(L))/(24*float(E)*float(I))
                print("Displacement at A due to applied loading, Slope(A1) = (W*L^3)/(24*E*I) = " + str(thetaA1))
                print("Displacement at B due to applied loading, Slope(B1) = -(W*L^3)/(24*E*I) = " + str(thetaB1) + " (Taking clockwise direction as negative)")

                print("\nSTEP 03: REMOVING LOADING AND CALCULATING DISPLACEMENT DUE TO REDUNDANT REACTIONS")
                print("Let 'Ma' be the redundant reaction at A and 'Mb' be the redundant reaction at B.")
                Ma = (float(W)*float(L)*float(L))/12
                thetaA2 = -(float(Ma)*float(L))/(3*float(E)*float(I))
                thetaB2 = (float(Ma)*float(L))/(6*float(E)*float(I))
                print("Displacement at A due to redundant reaction at A, Slope(A2) = -(Ma*L)/(3*E*I) = " + str(thetaA2) + " (Taking clockwise direction as negative)")
                print("Displacement at B due to redundant reaction at A, Slope(B2) = (Ma*L)/(6*E*I) = " + str(thetaB2))
                Mb = (float(W)*float(L)*float(L))/12
                thetaA3 = -(float(Mb)*float(L))/(6*float(E)*float(I))
                thetaB3 = (float(Mb)*float(L))/(3*float(E)*float(I))
                print("\nDisplacement at A due to redundant reaction at B, Slope(A3) = -(Mb*L)/(6*E*I) = " + str(thetaA3) + " (Taking clockwise direction as negative)")
                print("Displacement at B due to redundant reaction at B, Slope(B3) = (Mb*L)/(3*E*I) = " + str(thetaB3))

                print("\nSTEP 04: OBTAINING COMPATIBILITY EQUATION AND SOLVING FOR 'Ma' and 'Mb'")
                print("Approach:- To solve for redundant reactions, we need one more equation which can be obtained by compatability. It is quite evident that the displacement at the fixed supports A and B is zero.")
                print("Therefore, total displacement at A, Slope(A) = Slope(A1) + Slope(A2) + Slope(A3) = 0")
                print("Also, total displacement at B, Slope(B) = Slope(B1) + Slope(B2) + Slope(B3) = 0")
                print("Solving the above two equations, we get redundant reaction at A, Ma = (W*L^2)/12 = " + str(Ma) + " N")
                print("Redundant reaction at B, Mb = (W*L^2)/12 = " + str(Mb) + " N")

                # User is asked whether he or she wishes to continue the analysis or not
                choice = input("\nPlease enter 'y' if you wish to continue and 'n' to discontinue the anlaysis : ")

# If the user doesn't wish to continue with the program for beam analysis then the following else statement will be executed
else:
    print(exit)
    exit()
