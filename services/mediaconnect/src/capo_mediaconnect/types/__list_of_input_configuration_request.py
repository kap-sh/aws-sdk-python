"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfInputConfigurationRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.input_configuration_request

__listOfInputConfigurationRequest: TypeAlias = list[
    "capo_mediaconnect.types.input_configuration_request.InputConfigurationRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputConfigurationRequest) -> list:
    import capo_mediaconnect.types.input_configuration_request

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.input_configuration_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfInputConfigurationRequest:
    import capo_mediaconnect.types.input_configuration_request

    out: __listOfInputConfigurationRequest = []
    for item in data:
        out.append(
            capo_mediaconnect.types.input_configuration_request.deserialize_json(item)
        )
    return out
