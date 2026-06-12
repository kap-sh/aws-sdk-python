"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputDeviceSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_device_summary

__listOfInputDeviceSummary: TypeAlias = list[
    "aws_sdk_medialive.types.input_device_summary.InputDeviceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputDeviceSummary) -> list:
    import aws_sdk_medialive.types.input_device_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.input_device_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputDeviceSummary:
    import aws_sdk_medialive.types.input_device_summary

    out: __listOfInputDeviceSummary = []
    for item in data:
        out.append(aws_sdk_medialive.types.input_device_summary.deserialize_json(item))
    return out
