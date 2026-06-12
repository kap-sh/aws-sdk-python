"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.channel


class UpdateChannelResponse(TypedDict):
    channel: NotRequired["aws_sdk_medialive.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelResponse) -> dict:
    out: dict = {}
    if "channel" in value:
        import aws_sdk_medialive.types.channel

        out["channel"] = aws_sdk_medialive.types.channel.serialize_json(
            value["channel"]
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelResponse:
    out: UpdateChannelResponse = {}  # type: ignore[typeddict-item]
    if "channel" in data:
        import aws_sdk_medialive.types.channel

        out["channel"] = aws_sdk_medialive.types.channel.deserialize_json(
            data["channel"]
        )
    return out
