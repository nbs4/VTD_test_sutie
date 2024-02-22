# kvm_unit_test_suite
The KVM Unit Test suite is a collection of programs and scripts designed to test the functionality of the Kernel-based Virtual Machine (KVM) in the System Under Test (SUT). KVM is a full virtualization solution for Linux on hardware containing virtualization extensions (Intel VT).

**Virtualization_Super_Pages_L = ./tests/smap** - 
The Virtualization_Super_Pages_L test in the KVM unit test suite, when used with ./tests/smap, is likely designed to test the functionality of "super pages" or "large pages" in a virtualized environment with specific focus on Supervisor Mode Access Prevention (SMAP).
SMAP is a security feature of some modern processors that prevents the supervisor mode code (the kernel) from accessing user-space memory. This can help prevent certain types of security vulnerabilities where a bug in the kernel allows an attacker to manipulate kernel code to read or write to user-space memory.

**Virtualization_RealMode_L = ./tests/realmode** -
The Virtualization_RealMode_L test in the KVM unit test suite, when used with ./tests/realmode, is designed to test the functionality of "real mode" operation in a virtualized environment.
Real mode, also called real address mode, is an operating mode of all x86-compatible CPUs. Real mode is characterized by a 20-bit segmented memory address space (giving exactly 1 MiB of addressable memory) and unlimited direct software access to all addressable memory, I/O addresses and peripheral hardware. Real mode provides no support for memory protection, multitasking, or code privilege levels.

**Virtualization_Posted_interrupt_L = ./tests/vmx** - 
The Virtualization_Posted_interrupt_L test in the KVM unit test suite, when used with ./tests/vmx, is designed to test the functionality of "posted interrupts" in a virtualized environment.
Posted interrupts is a feature of some modern processors that improves the performance of virtual machines (VMs) by reducing the overhead of interrupt delivery. Normally, when a VM receives an interrupt, the hypervisor needs to intervene to deliver the interrupt to the VM. This can be a significant source of overhead, especially for workloads that generate a large number of interrupts.
Posted interrupts allow the hardware to deliver interrupts directly to a VM without hypervisor intervention. This can significantly improve the performance of interrupt-heavy workloads running in a VM.

**Virtualization_IR-QI_L = ./tests/intel_iommu** - 
The Virtualization_IR-QI_L test in the KVM unit test suite, when used with ./tests/intel_iommu, is designed to test the functionality of "Interrupt Remapping and Queued Invalidations (IR-QI)" in a virtualized environment.
Interrupt Remapping (IR) and Queued Invalidations (QI) are features of the Intel IOMMU (Input/Output Memory Management Unit) used in virtualization.
  * Interrupt Remapping (IR): This is a security feature that provides isolation of interrupt delivery between different virtual machines. It allows the IOMMU to change the routing of interrupts in a system, which can prevent one VM from interfering with the interrupts of another VM.
  * Queued Invalidations (QI): This is a performance feature that allows the IOMMU to queue invalidation requests, which can improve the performance of operations that require a large number of invalidations.

**Virtualization_EPT_subpage_protection_L = ./tests/vmx** - 
The Virtualization_Linux_EPT_subpage_protection_L test in the KVM unit test suite, when used with ./tests/vmx, is designed to test the functionality of "Extended Page Table (EPT) subpage protection" in a virtualized environment.
Extended Page Tables (EPT) is a memory management technology for hardware-assisted virtualization. EPT allows a guest operating system to modify its own page tables directly, which can significantly improve performance by reducing the number of VM exits.
Subpage protection is a feature that allows different permissions to be set for different parts of a memory page. This can provide more fine-grained control over memory access in a virtual machine.

**Virtualization_Virtualization_5-levelpagetables_L = ./tests/access** - 
The Virtualization_5-levelpagetables_L test in the KVM unit test suite, when used with ./tests/access, is designed to test the functionality of "5-level page tables" in a virtualized environment.
5-level page tables is a feature of some modern processors that allows for a larger virtual address space. Traditionally, x86 processors used a 4-level page table structure, which provides a 48-bit virtual address space. With 5-level page tables, this is extended to a 57-bit virtual address space, allowing for a much larger amount of virtual memory.
