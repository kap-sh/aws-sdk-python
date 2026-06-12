"""Generated from Smithy shape ``com.amazonaws.opensearch#ApplicationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.application_summary

ApplicationSummaries: TypeAlias = list[
    "aws_sdk_opensearch.types.application_summary.ApplicationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummaries) -> list:
    import aws_sdk_opensearch.types.application_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_opensearch.types.application_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationSummaries:
    import aws_sdk_opensearch.types.application_summary

    out: ApplicationSummaries = []
    for item in data:
        out.append(aws_sdk_opensearch.types.application_summary.deserialize_json(item))
    return out
