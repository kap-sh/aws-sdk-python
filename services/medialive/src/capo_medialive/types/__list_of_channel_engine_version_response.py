"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfChannelEngineVersionResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.channel_engine_version_response

__listOfChannelEngineVersionResponse: TypeAlias = list[
    "capo_medialive.types.channel_engine_version_response.ChannelEngineVersionResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfChannelEngineVersionResponse) -> list:
    import capo_medialive.types.channel_engine_version_response

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.channel_engine_version_response.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfChannelEngineVersionResponse:
    import capo_medialive.types.channel_engine_version_response

    out: __listOfChannelEngineVersionResponse = []
    for item in data:
        out.append(
            capo_medialive.types.channel_engine_version_response.deserialize_json(item)
        )
    return out
