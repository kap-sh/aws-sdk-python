"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#AppInstanceUserMembershipSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_type
    import capo_chime_sdk_messaging.types.sub_channel_id
    import capo_chime_sdk_messaging.types.timestamp


class AppInstanceUserMembershipSummary(TypedDict, closed=True):
    type: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
    ]
    """<p>The type of <code>ChannelMembership</code>.</p>"""
    read_marker_timestamp: NotRequired[
        "capo_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which an <code>AppInstanceUser</code> last marked a channel as read.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel that the <code>AppInstanceUser</code> is a member of.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceUserMembershipSummary) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_chime_sdk_messaging.types.channel_membership_type

        out["Type"] = (
            capo_chime_sdk_messaging.types.channel_membership_type.serialize_json(
                value["type"]
            )
        )
    if "read_marker_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["ReadMarkerTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["read_marker_timestamp"]
            )
        )
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> AppInstanceUserMembershipSummary:
    out: AppInstanceUserMembershipSummary = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_chime_sdk_messaging.types.channel_membership_type

        out["type"] = (
            capo_chime_sdk_messaging.types.channel_membership_type.deserialize_json(
                data["Type"]
            )
        )
    if "ReadMarkerTimestamp" in data:
        import capo_chime_sdk_messaging.types.timestamp

        out["read_marker_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["ReadMarkerTimestamp"]
            )
        )
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    return out
