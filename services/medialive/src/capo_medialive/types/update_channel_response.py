"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.channel


class UpdateChannelResponse(TypedDict, closed=True):
    channel: NotRequired["capo_medialive.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelResponse) -> dict:
    out: dict = {}
    if "channel" in value:
        import capo_medialive.types.channel

        out["channel"] = capo_medialive.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> UpdateChannelResponse:
    out: UpdateChannelResponse = {}  # type: ignore[typeddict-item]
    if "channel" in data:
        import capo_medialive.types.channel

        out["channel"] = capo_medialive.types.channel.deserialize_json(data["channel"])
    return out
