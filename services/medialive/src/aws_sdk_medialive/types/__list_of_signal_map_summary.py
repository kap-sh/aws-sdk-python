"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfSignalMapSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.signal_map_summary

__listOfSignalMapSummary: TypeAlias = list[
    "aws_sdk_medialive.types.signal_map_summary.SignalMapSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSignalMapSummary) -> list:
    import aws_sdk_medialive.types.signal_map_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.signal_map_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSignalMapSummary:
    import aws_sdk_medialive.types.signal_map_summary

    out: __listOfSignalMapSummary = []
    for item in data:
        out.append(aws_sdk_medialive.types.signal_map_summary.deserialize_json(item))
    return out
