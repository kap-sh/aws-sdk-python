"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationsAccessForOrganization``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.access_status


class NotificationsAccessForOrganization(TypedDict, closed=True):
    access_status: "aws_sdk_notifications.types.access_status.AccessStatus"
    """<p>Access Status for the Orgs Service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationsAccessForOrganization) -> dict:
    out: dict = {}
    import aws_sdk_notifications.types.access_status

    out["accessStatus"] = aws_sdk_notifications.types.access_status.serialize_json(
        value["access_status"]
    )
    return out


def deserialize_json(data: dict) -> NotificationsAccessForOrganization:
    out: NotificationsAccessForOrganization = {}  # type: ignore[typeddict-item]
    if "accessStatus" in data:
        import aws_sdk_notifications.types.access_status

        out["access_status"] = (
            aws_sdk_notifications.types.access_status.deserialize_json(
                data["accessStatus"]
            )
        )
    else:
        raise DeserializationError(
            "NotificationsAccessForOrganization.access_status required"
        )
    return out
