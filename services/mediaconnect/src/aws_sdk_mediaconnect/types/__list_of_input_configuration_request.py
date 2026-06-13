"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfInputConfigurationRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.input_configuration_request

__listOfInputConfigurationRequest: TypeAlias = list[
    "aws_sdk_mediaconnect.types.input_configuration_request.InputConfigurationRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputConfigurationRequest) -> list:
    import aws_sdk_mediaconnect.types.input_configuration_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.input_configuration_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfInputConfigurationRequest:
    import aws_sdk_mediaconnect.types.input_configuration_request

    out: __listOfInputConfigurationRequest = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.input_configuration_request.deserialize_json(
                item
            )
        )
    return out
