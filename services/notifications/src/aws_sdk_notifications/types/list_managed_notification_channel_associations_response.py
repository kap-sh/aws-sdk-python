"""Generated from Smithy shape ``com.amazonaws.notifications#ListManagedNotificationChannelAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_notifications.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_notifications.types.managed_notification_channel_associations
    import aws_sdk_notifications.types.next_token

class ListManagedNotificationChannelAssociationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    channel_associations: "aws_sdk_notifications.types.managed_notification_channel_associations.ManagedNotificationChannelAssociations"
    """<p>A list that contains the following information about a channel association.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListManagedNotificationChannelAssociationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_notifications.types.managed_notification_channel_associations
    out["channelAssociations"] = aws_sdk_notifications.types.managed_notification_channel_associations.serialize_json(value["channel_associations"])
    return out


def deserialize_json(data: dict) -> ListManagedNotificationChannelAssociationsResponse:
    out: ListManagedNotificationChannelAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "channelAssociations" in data:
        import aws_sdk_notifications.types.managed_notification_channel_associations
        out["channel_associations"] = aws_sdk_notifications.types.managed_notification_channel_associations.deserialize_json(data["channelAssociations"])
    else:
        raise DeserializationError("ListManagedNotificationChannelAssociationsResponse.channel_associations required")
    return out