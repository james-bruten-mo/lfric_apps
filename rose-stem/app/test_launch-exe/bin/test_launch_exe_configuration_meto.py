##############################################################################
# (c) Crown copyright 2025 Met Office. All rights reserved.
# The file LICENCE, distributed with this code, contains details of the terms
# under which the code may be used.
##############################################################################

import os
import subprocess
import unittest

class TestLaunchExeEnv(unittest.TestCase):
    launch_exe = os.environ["launch_exe_meto_path"]

    def test_run_shallow_water_williamson5_C24_azspice_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-azspice"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "1"
        os.environ["NUMA_REGIONS_PER_NODE"] = "0"
        os.environ["OMP_NUM_THREADS"] = "3"
        os.environ["TOTAL_RANKS"] = "6"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/shallow_water/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "shallow_water"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec -n 6 $OUTPUT_ROOT/bin/shallow_water/gnu_fast-debug-64bit/shallow_water configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_lfric_atm_nwp_gal9_C48_MG_azspice_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-azspice"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "1"
        os.environ["NUMA_REGIONS_PER_NODE"] = "0"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "24"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/lfric_atm/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "lfric_atm"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec -n 24 $OUTPUT_ROOT/bin/lfric_atm/gnu_fast-debug-64bit/lfric_atm configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_shallow_water_vortex_plane_BiP64x64_1x1_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "6"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/shallow_water/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "shallow_water"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 6 --depth 1 $OUTPUT_ROOT/bin/shallow_water/gnu_fast-debug-64bit/shallow_water configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_sbr_lam_n96_MG_lam_rotate_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "6"
        os.environ["TOTAL_RANKS"] = "4"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 4 --ppn 4 --depth 6 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_skamarock_klemp_gw_ph1pv0_BiP75x4_4000x2000_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "2"
        os.environ["TOTAL_RANKS"] = "6"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 6 --ppn 6 --depth 2 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_straka_200m_alt1_BiP256x4_200x200_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "8"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 8 --depth 1 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_lfric_atm_scm_ral3_urban2t_BiP2x2_50000x50000_azspice_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-azspice"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "1"
        os.environ["NUMA_REGIONS_PER_NODE"] = "0"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "1"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/lfric_atm/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "lfric_atm"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec -n 1 $OUTPUT_ROOT/bin/lfric_atm/gnu_fast-debug-64bit/lfric_atm configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_lfric_atm_nwp_gal9_mgnoukca_C48_MG_ex1a_cce_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "2"
        os.environ["TOTAL_RANKS"] = "12"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/lfric_atm/cce_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "lfric_atm"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 12 --ppn 12 --depth 2 $OUTPUT_ROOT/bin/lfric_atm/cce_fast-debug-64bit/lfric_atm configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_linear_model_runge_kutta_C12_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "1"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/linear_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "linear_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 1 --depth 1 $OUTPUT_ROOT/bin/linear_model/gnu_fast-debug-64bit/linear_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_lfric_atm_ral3_ens_seuk_MG_ex1a_cce_fast_debug_64bit_crun1(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "16"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/lfric_atm/cce_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "lfric_atm"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 16 --depth 1 $OUTPUT_ROOT/bin/lfric_atm/cce_fast-debug-64bit/lfric_atm configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_shallow_water_galewsky_vi_ffsl_C96_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "3"
        os.environ["TOTAL_RANKS"] = "6"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/shallow_water/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "shallow_water"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 6 --ppn 6 --depth 3 $OUTPUT_ROOT/bin/shallow_water/gnu_fast-debug-64bit/shallow_water configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_transport_eternal_fountain_xz_split_vhv_BiP100x10_20x20_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "5"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/transport/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "transport"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 5 --depth 1 $OUTPUT_ROOT/bin/transport/gnu_fast-debug-64bit/transport configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_transport_cylinder_xz_split_BiP100x10_20x20_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "4"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/transport/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "transport"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 4 --depth 1 $OUTPUT_ROOT/bin/transport/gnu_fast-debug-64bit/transport configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_lfric_atm_ral3_seuk_MG_azspice_gnu_fast_debug_64bit_crun1(self):
        os.environ["TARGET_PLATFORM"] = "meto-azspice"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "1"
        os.environ["NUMA_REGIONS_PER_NODE"] = "0"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "16"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/lfric_atm/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "lfric_atm"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec -n 16 $OUTPUT_ROOT/bin/lfric_atm/gnu_fast-debug-64bit/lfric_atm configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_lfric_atm_nwp_gal9_C48_MG_ex1a_cce_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "54"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/lfric_atm/cce_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "lfric_atm"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 54 --depth 1 $OUTPUT_ROOT/bin/lfric_atm/cce_fast-debug-64bit/lfric_atm configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_straka_200m_BiP256x8_200x200_azspice_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-azspice"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "1"
        os.environ["NUMA_REGIONS_PER_NODE"] = "0"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "8"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec -n 8 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_transport_hadley_dcmip_ffsl_C48_azspice_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-azspice"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "1"
        os.environ["NUMA_REGIONS_PER_NODE"] = "0"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "12"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/transport/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "transport"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec -n 12 $OUTPUT_ROOT/bin/transport/gnu_fast-debug-64bit/transport configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_baroclinic_C192_MG_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "384"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 384 --ppn 128 --depth 1 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_lfric_atm_nwp_gal9_debug_C48_MG_ex1a_gnu_full_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "24"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/lfric_atm/gnu_full-debug-64bit"
        os.environ["EXEC_NAME"] = "lfric_atm"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 24 --depth 1 $OUTPUT_ROOT/bin/lfric_atm/gnu_full-debug-64bit/lfric_atm configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_skamarock_klemp_gw_p1_BiP75x4_4000x2000_azspice_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-azspice"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "1"
        os.environ["NUMA_REGIONS_PER_NODE"] = "0"
        os.environ["OMP_NUM_THREADS"] = "2"
        os.environ["TOTAL_RANKS"] = "3"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec -n 3 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_lfric_real_domain_C48_MG_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "4"
        os.environ["TOTAL_RANKS"] = "6"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 6 --ppn 6 --depth 4 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_skamarock_klemp_gw_p1_BiP75x4_4000x2000_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "2"
        os.environ["TOTAL_RANKS"] = "3"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 3 --ppn 3 --depth 2 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_bryan_fritsch_dry_BiP200x10_100x100_azspice_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-azspice"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "1"
        os.environ["NUMA_REGIONS_PER_NODE"] = "0"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "10"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec -n 10 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_robert_moist_smag_BiP100x8_10x10_azspice_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-azspice"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "1"
        os.environ["NUMA_REGIONS_PER_NODE"] = "0"
        os.environ["OMP_NUM_THREADS"] = "2"
        os.environ["TOTAL_RANKS"] = "5"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec -n 5 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_linear_model_dcmip301_C24_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "12"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/linear_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "linear_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 12 --depth 1 $OUTPUT_ROOT/bin/linear_model/gnu_fast-debug-64bit/linear_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_bryan_fritsch_dry_BiP200x10_100x100_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "10"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 10 --depth 1 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_transport_cylinder_xz_ffsl_BiP100x10_20x20_azspice_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-azspice"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "1"
        os.environ["NUMA_REGIONS_PER_NODE"] = "0"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "4"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/transport/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "transport"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec -n 4 $OUTPUT_ROOT/bin/transport/gnu_fast-debug-64bit/transport configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_robert_moist_smag_BiP100x8_10x10_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "2"
        os.environ["TOTAL_RANKS"] = "5"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 5 --ppn 5 --depth 2 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_gungho_model_schar_cart_alt2_BiP100x4_1000x1000_ex1a_gnu_fast_debug_64bit(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "3"
        os.environ["TOTAL_RANKS"] = "5"
        os.environ["XIOS_SERVER_MODE"] = "False"
        os.environ["XIOS_SERVER_RANKS"] = "0"
        os.environ["xios_nodes"] = "0"
        os.environ["mpi_parts_xios"] = "0"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit"
        os.environ["EXEC_NAME"] = "gungho_model"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 5 --ppn 5 --depth 3 $OUTPUT_ROOT/bin/gungho_model/gnu_fast-debug-64bit/gungho_model configuration.nml "
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

    def test_run_lfric_atm_nwp_gal9_C224_MG_ex1a_cce_fast_debug_64bit_rbl32(self):
        os.environ["TARGET_PLATFORM"] = "meto-ex1a"
        os.environ["RUN_METHOD"] = "mpiexec"
        os.environ["HYPERTHREADS"] = "1"
        os.environ["CORES_PER_NODE"] = "128"
        os.environ["NUMA_REGIONS_PER_NODE"] = "2"
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["TOTAL_RANKS"] = "1176"
        os.environ["XIOS_SERVER_MODE"] = "True"
        os.environ["XIOS_SERVER_RANKS"] = "16"
        os.environ["xios_nodes"] = "4"
        os.environ["mpi_parts_xios"] = "16"
        os.environ["CORES_PER_NODE_OVERRIDE"] = "0"
        os.environ["BIN_DIR"] = "$OUTPUT_ROOT/bin/lfric_atm/cce_fast-debug-64bit-rbl32"
        os.environ["EXEC_NAME"] = "lfric_atm"
        os.environ["PAT_EXE_EXTEN"] = ""
        os.environ["TEST_LAUNCH_EXE_EXEC"] = "mpiexec --cpu-bind=depth --np 1176 --ppn 128 --depth 1 $OUTPUT_ROOT/bin/lfric_atm/cce_fast-debug-64bit-rbl32/lfric_atm configuration.nml  : --cpu-bind=depth --np 16 --ppn 4 xios_server.exe"
        sr = subprocess.run(self.launch_exe,
                            capture_output=True)
        if sr.returncode == 0:
            self.assertTrue
        else:
            self.assertFalse(f"{sr.stderr}")

