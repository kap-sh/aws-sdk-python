"""Generated from Smithy shape ``com.amazonaws.ec2#MacSystemIntegrityProtectionConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status


class MacSystemIntegrityProtectionConfigurationRequest(TypedDict):
    apple_internal: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Enables or disables Apple Internal.</p>"""
    base_system: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Enables or disables Base System.</p>"""
    debugging_restrictions: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Enables or disables Debugging Restrictions.</p>"""
    d_trace_restrictions: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Enables or disables Dtrace Restrictions.</p>"""
    filesystem_protections: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Enables or disables Filesystem Protections.</p>"""
    kext_signing: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Enables or disables Kext Signing.</p>"""
    nvram_protections: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Enables or disables Nvram Protections.</p>"""
