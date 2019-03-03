"""Tests for getters."""

from napalm.base.test.getters import BaseTestGetters
from napalm.base.test import helpers
from napalm.base.test.getters import wrap_test_cases
from napalm.base.utils.py23_compat import text_type

import pytest


@pytest.mark.usefixtures("set_device_parameters")
class TestGetter(BaseTestGetters):
    """Test get_* methods."""

    @wrap_test_cases
    def test_get_facts(self, test_case):
        """Test get_facts method."""
        modale_facts = {
            "os_version": text_type,
            "uptime": int,
            "interface_list": list,
            "vendor": text_type,
            "model": text_type,
            "hostname": text_type,
        }
        facts = self.device.get_facts()
        assert helpers.test_model(modale_facts, facts)
        return facts