"""Generated from Smithy shape ``com.amazonaws.ec2#MacSystemIntegrityProtectionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status


class MacSystemIntegrityProtectionConfiguration(TypedDict):
    apple_internal: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Apple Internal was enabled or disabled by the task.</p>"""
    base_system: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Base System was enabled or disabled by the task.</p>"""
    debugging_restrictions: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Debugging Restrictions was enabled or disabled by the task.</p>"""
    d_trace_restrictions: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Dtrace Restrictions was enabled or disabled by the task.</p>"""
    filesystem_protections: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Filesystem Protections was enabled or disabled by the task.</p>"""
    kext_signing: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Kext Signing was enabled or disabled by the task.</p>"""
    nvram_protections: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether NVRAM Protections was enabled or disabled by the task.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates SIP was enabled or disabled by the task.</p>"""
