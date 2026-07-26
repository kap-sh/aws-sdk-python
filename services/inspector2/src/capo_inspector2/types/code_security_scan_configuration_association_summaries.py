"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSecurityScanConfigurationAssociationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.code_security_scan_configuration_association_summary

CodeSecurityScanConfigurationAssociationSummaries: TypeAlias = list[
    "capo_inspector2.types.code_security_scan_configuration_association_summary.CodeSecurityScanConfigurationAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeSecurityScanConfigurationAssociationSummaries) -> list:
    import capo_inspector2.types.code_security_scan_configuration_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_inspector2.types.code_security_scan_configuration_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CodeSecurityScanConfigurationAssociationSummaries:
    import capo_inspector2.types.code_security_scan_configuration_association_summary

    out: CodeSecurityScanConfigurationAssociationSummaries = []
    for item in data:
        out.append(
            capo_inspector2.types.code_security_scan_configuration_association_summary.deserialize_json(
                item
            )
        )
    return out
