"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfInputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.input_configuration

__listOfInputConfiguration: TypeAlias = list[
    "capo_mediaconnect.types.input_configuration.InputConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputConfiguration) -> list:
    import capo_mediaconnect.types.input_configuration

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.input_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputConfiguration:
    import capo_mediaconnect.types.input_configuration

    out: __listOfInputConfiguration = []
    for item in data:
        out.append(capo_mediaconnect.types.input_configuration.deserialize_json(item))
    return out
