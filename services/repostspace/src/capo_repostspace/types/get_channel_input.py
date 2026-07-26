"""Generated from Smithy shape ``com.amazonaws.repostspace#GetChannelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.channel_id
    import capo_repostspace.types.space_id


class GetChannelInput(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    channel_id: "capo_repostspace.types.channel_id.ChannelId"
    """<p>The unique ID of the private re:Post channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChannelInput:
    out: GetChannelInput = {}  # type: ignore[typeddict-item]
    return out
