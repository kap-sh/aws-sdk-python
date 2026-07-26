"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSecurityScanConfigurationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.code_security_scan_configuration_summary

CodeSecurityScanConfigurationSummaries: TypeAlias = list[
    "capo_inspector2.types.code_security_scan_configuration_summary.CodeSecurityScanConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeSecurityScanConfigurationSummaries) -> list:
    import capo_inspector2.types.code_security_scan_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_inspector2.types.code_security_scan_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CodeSecurityScanConfigurationSummaries:
    import capo_inspector2.types.code_security_scan_configuration_summary

    out: CodeSecurityScanConfigurationSummaries = []
    for item in data:
        out.append(
            capo_inspector2.types.code_security_scan_configuration_summary.deserialize_json(
                item
            )
        )
    return out
