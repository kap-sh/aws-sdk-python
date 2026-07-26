"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputDeviceSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.input_device_summary

__listOfInputDeviceSummary: TypeAlias = list[
    "capo_medialive.types.input_device_summary.InputDeviceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputDeviceSummary) -> list:
    import capo_medialive.types.input_device_summary

    out: list = []
    for item in value:
        out.append(capo_medialive.types.input_device_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputDeviceSummary:
    import capo_medialive.types.input_device_summary

    out: __listOfInputDeviceSummary = []
    for item in data:
        out.append(capo_medialive.types.input_device_summary.deserialize_json(item))
    return out
