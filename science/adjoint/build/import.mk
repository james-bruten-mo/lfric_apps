##############################################################################
# (c) Crown copyright 2023-2024 Met Office. All rights reserved.
# The file LICENCE, distributed with this code, contains details of the terms
# under which the code may be used.
##############################################################################
PROJECT_SOURCE = $(APPS_ROOT_DIR)/science/adjoint/source

.PHONY: import-adjoint
import-adjoint:
	$Q$(MAKE) $(QUIET_ARG) -f $(LFRIC_BUILD)/extract.mk \
	          SOURCE_DIR=$(PROJECT_SOURCE)
	$Q$(MAKE) $(QUIET_ARG) -f $(LFRIC_BUILD)/psyclone/psyclone_psykal.mk \
	          SOURCE_DIR=$(PROJECT_SOURCE) \
	          OPTIMISATION_PATH=$(OPTIMISATION_PATH)
##############################################################################
# Need this step to PSyclone the generated adjoint tests from PSyAD
ifeq "$(BUILD_ADJ_TESTS)" "TRUE"
	$Q$(MAKE) $(QUIET_ARG) -f $(LFRIC_BUILD)/psyclone/psyclone_psykal.mk \
	          SOURCE_DIR=$(WORKING_DIR) \
	          OPTIMISATION_PATH=$(OPTIMISATION_PATH) \
	          PSYCLONE_CONFIG_FILE=$(PSYAD_CONFIG_FILE)
endif

