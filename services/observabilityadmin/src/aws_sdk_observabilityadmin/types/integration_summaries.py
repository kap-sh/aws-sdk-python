"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#IntegrationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.integration_summary

IntegrationSummaries: TypeAlias = list[
    "aws_sdk_observabilityadmin.types.integration_summary.IntegrationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummaries) -> list:
    import aws_sdk_observabilityadmin.types.integration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_observabilityadmin.types.integration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IntegrationSummaries:
    import aws_sdk_observabilityadmin.types.integration_summary

    out: IntegrationSummaries = []
    for item in data:
        out.append(
            aws_sdk_observabilityadmin.types.integration_summary.deserialize_json(item)
        )
    return out
