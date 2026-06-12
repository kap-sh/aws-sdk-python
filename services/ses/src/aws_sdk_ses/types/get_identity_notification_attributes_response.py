"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityNotificationAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.notification_attributes


class GetIdentityNotificationAttributesResponse(TypedDict):
    notification_attributes: (
        "aws_sdk_ses.types.notification_attributes.NotificationAttributes"
    )
    """<p>A map of Identity to IdentityNotificationAttributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityNotificationAttributesResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_ses.types.notification_attributes

    aws_sdk_ses.types.notification_attributes.serialize_query(
        value["notification_attributes"], pairs, f"{prefix}.NotificationAttributes"
    )


def deserialize_query(el: Element) -> GetIdentityNotificationAttributesResponse:
    out: GetIdentityNotificationAttributesResponse = {}  # type: ignore[typeddict-item]
    child_notification_attributes = el.find("NotificationAttributes")
    if child_notification_attributes is not None:
        import aws_sdk_ses.types.notification_attributes

        out["notification_attributes"] = (
            aws_sdk_ses.types.notification_attributes.deserialize_query(
                child_notification_attributes
            )
        )
    else:
        raise DeserializationError(
            "GetIdentityNotificationAttributesResponse.notification_attributes required"
        )
    return out
