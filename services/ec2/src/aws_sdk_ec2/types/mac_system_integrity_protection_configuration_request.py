"""Generated from Smithy shape ``com.amazonaws.ec2#MacSystemIntegrityProtectionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status


class MacSystemIntegrityProtectionConfigurationRequest(TypedDict, closed=True):
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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MacSystemIntegrityProtectionConfigurationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "apple_internal" in value:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["apple_internal"], pairs, f"{prefix}.AppleInternal"
        )
    if "base_system" in value:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["base_system"], pairs, f"{prefix}.BaseSystem"
        )
    if "debugging_restrictions" in value:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["debugging_restrictions"], pairs, f"{prefix}.DebuggingRestrictions"
        )
    if "d_trace_restrictions" in value:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["d_trace_restrictions"], pairs, f"{prefix}.DTraceRestrictions"
        )
    if "filesystem_protections" in value:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["filesystem_protections"], pairs, f"{prefix}.FilesystemProtections"
        )
    if "kext_signing" in value:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["kext_signing"], pairs, f"{prefix}.KextSigning"
        )
    if "nvram_protections" in value:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["nvram_protections"], pairs, f"{prefix}.NvramProtections"
        )


def deserialize_ec2_query(
    el: Element,
) -> MacSystemIntegrityProtectionConfigurationRequest:
    out: MacSystemIntegrityProtectionConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_apple_internal = el.find("AppleInternal")
    if child_apple_internal is not None:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        out["apple_internal"] = (
            aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_apple_internal
            )
        )
    child_base_system = el.find("BaseSystem")
    if child_base_system is not None:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        out["base_system"] = (
            aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_base_system
            )
        )
    child_debugging_restrictions = el.find("DebuggingRestrictions")
    if child_debugging_restrictions is not None:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        out["debugging_restrictions"] = (
            aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_debugging_restrictions
            )
        )
    child_d_trace_restrictions = el.find("DTraceRestrictions")
    if child_d_trace_restrictions is not None:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        out["d_trace_restrictions"] = (
            aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_d_trace_restrictions
            )
        )
    child_filesystem_protections = el.find("FilesystemProtections")
    if child_filesystem_protections is not None:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        out["filesystem_protections"] = (
            aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_filesystem_protections
            )
        )
    child_kext_signing = el.find("KextSigning")
    if child_kext_signing is not None:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        out["kext_signing"] = (
            aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_kext_signing
            )
        )
    child_nvram_protections = el.find("NvramProtections")
    if child_nvram_protections is not None:
        import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status

        out["nvram_protections"] = (
            aws_sdk_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_nvram_protections
            )
        )
    return out
