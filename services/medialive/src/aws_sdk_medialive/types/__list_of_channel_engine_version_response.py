"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfChannelEngineVersionResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.channel_engine_version_response

__listOfChannelEngineVersionResponse: TypeAlias = list[
    "aws_sdk_medialive.types.channel_engine_version_response.ChannelEngineVersionResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfChannelEngineVersionResponse) -> list:
    import aws_sdk_medialive.types.channel_engine_version_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.channel_engine_version_response.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfChannelEngineVersionResponse:
    import aws_sdk_medialive.types.channel_engine_version_response

    out: __listOfChannelEngineVersionResponse = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.channel_engine_version_response.deserialize_json(
                item
            )
        )
    return out
