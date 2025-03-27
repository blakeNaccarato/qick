set windows-shell :=\
  ['powershell', '-NonInteractive', '-NoProfile', '-Command']

# Create demo project in Vivado 2023.1
[working-directory: 'firmware/projects/qick_tprocv2_216_demo']
create-demo-project:
  . 'C:/Xilinx/Vivado/2023.1/bin/vivado.bat' \
    -mode 'batch' \
    -source 'proj.tcl'
