"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SubChannelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.membership_count
    import capo_chime_sdk_messaging.types.sub_channel_id


class SubChannelSummary(TypedDict, closed=True):
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The unique ID of a SubChannel.</p>"""
    membership_count: NotRequired[
        "capo_chime_sdk_messaging.types.membership_count.MembershipCount"
    ]
    """<p>The number of members in a SubChannel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubChannelSummary) -> dict:
    out: dict = {}
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    if "membership_count" in value:
        out["MembershipCount"] = value["membership_count"]
    return out


def deserialize_json(data: dict) -> SubChannelSummary:
    out: SubChannelSummary = {}  # type: ignore[typeddict-item]
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    if "MembershipCount" in data:
        out["membership_count"] = data["MembershipCount"]
    return out
