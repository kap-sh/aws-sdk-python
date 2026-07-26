"""Generated from Smithy shape ``com.amazonaws.connect#DescribeNotificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.notification


class DescribeNotificationResponse(TypedDict, closed=True):
    notification: "capo_connect.types.notification.Notification"
    """<p>The complete notification information including content, priority, recipients, and metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNotificationResponse) -> dict:
    out: dict = {}
    import capo_connect.types.notification

    out["Notification"] = capo_connect.types.notification.serialize_json(
        value["notification"]
    )
    return out


def deserialize_json(data: dict) -> DescribeNotificationResponse:
    out: DescribeNotificationResponse = {}  # type: ignore[typeddict-item]
    if "Notification" in data:
        import capo_connect.types.notification

        out["notification"] = capo_connect.types.notification.deserialize_json(
            data["Notification"]
        )
    else:
        raise DeserializationError("DescribeNotificationResponse.notification required")
    return out
