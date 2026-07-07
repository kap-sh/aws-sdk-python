"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateChannelClassResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.channel


class UpdateChannelClassResponse(TypedDict, closed=True):
    channel: NotRequired["aws_sdk_medialive.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelClassResponse) -> dict:
    out: dict = {}
    if "channel" in value:
        import aws_sdk_medialive.types.channel

        out["channel"] = aws_sdk_medialive.types.channel.serialize_json(
            value["channel"]
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelClassResponse:
    out: UpdateChannelClassResponse = {}  # type: ignore[typeddict-item]
    if "channel" in data:
        import aws_sdk_medialive.types.channel

        out["channel"] = aws_sdk_medialive.types.channel.deserialize_json(
            data["channel"]
        )
    return out
