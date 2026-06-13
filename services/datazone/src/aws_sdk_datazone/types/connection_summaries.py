"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.connection_summary

ConnectionSummaries: TypeAlias = list[
    "aws_sdk_datazone.types.connection_summary.ConnectionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionSummaries) -> list:
    import aws_sdk_datazone.types.connection_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.connection_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectionSummaries:
    import aws_sdk_datazone.types.connection_summary

    out: ConnectionSummaries = []
    for item in data:
        out.append(aws_sdk_datazone.types.connection_summary.deserialize_json(item))
    return out
