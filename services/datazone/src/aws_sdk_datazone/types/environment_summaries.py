"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.environment_summary

EnvironmentSummaries: TypeAlias = list[
    "aws_sdk_datazone.types.environment_summary.EnvironmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentSummaries) -> list:
    import aws_sdk_datazone.types.environment_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.environment_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentSummaries:
    import aws_sdk_datazone.types.environment_summary

    out: EnvironmentSummaries = []
    for item in data:
        out.append(aws_sdk_datazone.types.environment_summary.deserialize_json(item))
    return out
