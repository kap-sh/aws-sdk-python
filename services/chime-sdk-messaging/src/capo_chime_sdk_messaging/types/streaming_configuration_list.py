"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#StreamingConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.streaming_configuration

StreamingConfigurationList: TypeAlias = list[
    "capo_chime_sdk_messaging.types.streaming_configuration.StreamingConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamingConfigurationList) -> list:
    import capo_chime_sdk_messaging.types.streaming_configuration

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_messaging.types.streaming_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StreamingConfigurationList:
    import capo_chime_sdk_messaging.types.streaming_configuration

    out: StreamingConfigurationList = []
    for item in data:
        out.append(
            capo_chime_sdk_messaging.types.streaming_configuration.deserialize_json(
                item
            )
        )
    return out
