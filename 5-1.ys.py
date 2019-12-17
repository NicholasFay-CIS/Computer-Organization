# Execution begins at address 0 
    .pos 0
    irmovq stack, %rsp      # Set up stack pointer
    call main       # Execute main program
    brk
    halt            # Terminate program 

# Array of 4 elements
    .align 8
array:  
    .quad 0x000000000012
    .quad 0x000000000011
    .quad 0x000000000010
    .quad 0x000000000009
    .quad 0x000000000008
    .quad 0x000000000007
    .quad 0x000000000006
    .quad 0x000000000005
    .quad 0x000000000004
    .quad 0x000000000003
    .quad 0x000000000002
    .quad 0x000000000001
    
main:   irmovq array, %rdi
    irmovq $12, %r8
    call sort       # calls sort
    ret
# start in %rdi, count in %rsi
sort:
    irmovq $0, %r10 # i = 0
    Loop1:
        irmovq $11, %r13 #put the array size - 1 in r13
        rrmovq %r10, %rbx
        subq %r13, %rbx  # subtracts i from 11
        jge END #j if not less than or equal
        irmovq $0, %r11 # j = 0
        #subq is equivalent to compare with sideeffects
    Loop2:
        irmovq $11, %r14 #put 11 in r14
        rrmovq %r11, %r12
        subq %r10, %r14  #array_size - 1 - i
        subq %r14, %r12  #j >= array_size - 1 - i
        jge ENDLoop1     #jump if j is greater than ^
        irmovq $8, %r9   #put 8 into register9 to add to rsi
        rrmovq %rdi, %rsi #put rdi's value in rsi
        addq %r9, %rsi
        mrmovq (%rdi), %rcx
        mrmovq (%rsi), %r12
        subq %r12, %rcx
        jl ENDLoop2  #jump if less than, for j
        call swap #call to swap function
        jmp ENDLoop2    #unconditional jump to Endloop2
    
    ENDLoop2:
        addq %r9, %rdi     #add 8 to rdi
        #irmovq $1, %r10
        irmovq $1, %rcx #increment by 1
        addq %rcx, %r11
        #irmovq $1, %r11
        jmp Loop2        #unconditional jump to loop2
    ENDLoop1:
        irmovq $1, %rcx      #increment by 1
        addq %rcx, %r10      #add 1 to i
        irmovq array, %rdi   #move array into rdi
        jmp Loop1            #unconditional jump to loop1
        
    END:
    ret
swap: 
    mrmovq (%rdi), %rax        # Put first pointer in register
    mrmovq (%rsi), %rdx        # Put second pointer in register 
    rmmovq %rdx, (%rdi)      # swap the first variable
    rmmovq %rax, (%rsi)      # swap the second variable
    ret                  #return 

# Stack starts here and grows to lower addresses
    .pos 0x200
stack: