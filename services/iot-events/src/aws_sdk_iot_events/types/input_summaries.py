"""Generated from Smithy shape ``com.amazonaws.iotevents#InputSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.input_summary

InputSummaries: TypeAlias = list["aws_sdk_iot_events.types.input_summary.InputSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: InputSummaries) -> list:
    import aws_sdk_iot_events.types.input_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_events.types.input_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> InputSummaries:
    import aws_sdk_iot_events.types.input_summary

    out: InputSummaries = []
    for item in data:
        out.append(aws_sdk_iot_events.types.input_summary.deserialize_json(item))
    return out
