"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputDeviceRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_device_request

__listOfInputDeviceRequest: TypeAlias = list[
    "aws_sdk_medialive.types.input_device_request.InputDeviceRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputDeviceRequest) -> list:
    import aws_sdk_medialive.types.input_device_request

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.input_device_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputDeviceRequest:
    import aws_sdk_medialive.types.input_device_request

    out: __listOfInputDeviceRequest = []
    for item in data:
        out.append(aws_sdk_medialive.types.input_device_request.deserialize_json(item))
    return out
