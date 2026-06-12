"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetChannelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.channels_response


class GetChannelsResponse(TypedDict):
    channels_response: NotRequired[
        "aws_sdk_pinpoint.types.channels_response.ChannelsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelsResponse) -> dict:
    out: dict = {}
    if "channels_response" in value:
        import aws_sdk_pinpoint.types.channels_response

        out["ChannelsResponse"] = (
            aws_sdk_pinpoint.types.channels_response.serialize_json(
                value["channels_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetChannelsResponse:
    out: GetChannelsResponse = {}  # type: ignore[typeddict-item]
    if "ChannelsResponse" in data:
        import aws_sdk_pinpoint.types.channels_response

        out["channels_response"] = (
            aws_sdk_pinpoint.types.channels_response.deserialize_json(
                data["ChannelsResponse"]
            )
        )
    return out
