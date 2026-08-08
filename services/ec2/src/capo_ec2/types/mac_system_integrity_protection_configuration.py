"""Generated from Smithy shape ``com.amazonaws.ec2#MacSystemIntegrityProtectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.mac_system_integrity_protection_setting_status


class MacSystemIntegrityProtectionConfiguration(TypedDict, closed=True):
    apple_internal: NotRequired[
        "capo_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Apple Internal was enabled or disabled by the task.</p>"""
    base_system: NotRequired[
        "capo_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Base System was enabled or disabled by the task.</p>"""
    debugging_restrictions: NotRequired[
        "capo_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Debugging Restrictions was enabled or disabled by the task.</p>"""
    d_trace_restrictions: NotRequired[
        "capo_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Dtrace Restrictions was enabled or disabled by the task.</p>"""
    filesystem_protections: NotRequired[
        "capo_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Filesystem Protections was enabled or disabled by the task.</p>"""
    kext_signing: NotRequired[
        "capo_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether Kext Signing was enabled or disabled by the task.</p>"""
    nvram_protections: NotRequired[
        "capo_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates whether NVRAM Protections was enabled or disabled by the task.</p>"""
    status: NotRequired[
        "capo_ec2.types.mac_system_integrity_protection_setting_status.MacSystemIntegrityProtectionSettingStatus"
    ]
    """<p>Indicates SIP was enabled or disabled by the task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MacSystemIntegrityProtectionConfiguration,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "apple_internal" in value:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        capo_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["apple_internal"], pairs, f"{key_prefix}AppleInternal"
        )
    if "base_system" in value:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        capo_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["base_system"], pairs, f"{key_prefix}BaseSystem"
        )
    if "debugging_restrictions" in value:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        capo_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["debugging_restrictions"], pairs, f"{key_prefix}DebuggingRestrictions"
        )
    if "d_trace_restrictions" in value:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        capo_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["d_trace_restrictions"], pairs, f"{key_prefix}DTraceRestrictions"
        )
    if "filesystem_protections" in value:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        capo_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["filesystem_protections"], pairs, f"{key_prefix}FilesystemProtections"
        )
    if "kext_signing" in value:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        capo_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["kext_signing"], pairs, f"{key_prefix}KextSigning"
        )
    if "nvram_protections" in value:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        capo_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["nvram_protections"], pairs, f"{key_prefix}NvramProtections"
        )
    if "status" in value:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        capo_ec2.types.mac_system_integrity_protection_setting_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_ec2_query(el: Element) -> MacSystemIntegrityProtectionConfiguration:
    out: MacSystemIntegrityProtectionConfiguration = {}  # type: ignore[typeddict-item]
    child_apple_internal = el.find("appleInternal")
    if child_apple_internal is not None:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        out["apple_internal"] = (
            capo_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_apple_internal
            )
        )
    child_base_system = el.find("baseSystem")
    if child_base_system is not None:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        out["base_system"] = (
            capo_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_base_system
            )
        )
    child_debugging_restrictions = el.find("debuggingRestrictions")
    if child_debugging_restrictions is not None:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        out["debugging_restrictions"] = (
            capo_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_debugging_restrictions
            )
        )
    child_d_trace_restrictions = el.find("dTraceRestrictions")
    if child_d_trace_restrictions is not None:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        out["d_trace_restrictions"] = (
            capo_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_d_trace_restrictions
            )
        )
    child_filesystem_protections = el.find("filesystemProtections")
    if child_filesystem_protections is not None:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        out["filesystem_protections"] = (
            capo_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_filesystem_protections
            )
        )
    child_kext_signing = el.find("kextSigning")
    if child_kext_signing is not None:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        out["kext_signing"] = (
            capo_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_kext_signing
            )
        )
    child_nvram_protections = el.find("nvramProtections")
    if child_nvram_protections is not None:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        out["nvram_protections"] = (
            capo_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_nvram_protections
            )
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.mac_system_integrity_protection_setting_status

        out["status"] = (
            capo_ec2.types.mac_system_integrity_protection_setting_status.deserialize_ec2_query(
                child_status
            )
        )
    return out
