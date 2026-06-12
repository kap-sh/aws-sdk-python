"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputDeviceSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_device_settings

__listOfInputDeviceSettings: TypeAlias = list[
    "aws_sdk_medialive.types.input_device_settings.InputDeviceSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputDeviceSettings) -> list:
    import aws_sdk_medialive.types.input_device_settings

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.input_device_settings.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputDeviceSettings:
    import aws_sdk_medialive.types.input_device_settings

    out: __listOfInputDeviceSettings = []
    for item in data:
        out.append(aws_sdk_medialive.types.input_device_settings.deserialize_json(item))
    return out
