"""Generated from Smithy shape ``com.amazonaws.connect#CreateNotificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.notification_id


class CreateNotificationResponse(TypedDict, closed=True):
    notification_id: "aws_sdk_connect.types.notification_id.NotificationId"
    """<p>The unique identifier assigned to the created notification.</p>"""
    notification_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the created notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationResponse) -> dict:
    out: dict = {}
    out["NotificationId"] = value["notification_id"]
    out["NotificationArn"] = value["notification_arn"]
    return out


def deserialize_json(data: dict) -> CreateNotificationResponse:
    out: CreateNotificationResponse = {}  # type: ignore[typeddict-item]
    if "NotificationId" in data:
        out["notification_id"] = data["NotificationId"]
    else:
        raise DeserializationError(
            "CreateNotificationResponse.notification_id required"
        )
    if "NotificationArn" in data:
        out["notification_arn"] = data["NotificationArn"]
    else:
        raise DeserializationError(
            "CreateNotificationResponse.notification_arn required"
        )
    return out
