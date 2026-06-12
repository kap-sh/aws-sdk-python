"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMultiplexSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.multiplex_summary

__listOfMultiplexSummary: TypeAlias = list[
    "aws_sdk_medialive.types.multiplex_summary.MultiplexSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMultiplexSummary) -> list:
    import aws_sdk_medialive.types.multiplex_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.multiplex_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMultiplexSummary:
    import aws_sdk_medialive.types.multiplex_summary

    out: __listOfMultiplexSummary = []
    for item in data:
        out.append(aws_sdk_medialive.types.multiplex_summary.deserialize_json(item))
    return out
