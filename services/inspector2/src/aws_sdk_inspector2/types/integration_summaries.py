"""Generated from Smithy shape ``com.amazonaws.inspector2#IntegrationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_integration_summary

IntegrationSummaries: TypeAlias = list[
    "aws_sdk_inspector2.types.code_security_integration_summary.CodeSecurityIntegrationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummaries) -> list:
    import aws_sdk_inspector2.types.code_security_integration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.code_security_integration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IntegrationSummaries:
    import aws_sdk_inspector2.types.code_security_integration_summary

    out: IntegrationSummaries = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.code_security_integration_summary.deserialize_json(
                item
            )
        )
    return out
