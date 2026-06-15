"""Generated from Smithy shape ``com.amazonaws.connect#SendNotificationActionDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.content
    import aws_sdk_connect.types.notification_content_type
    import aws_sdk_connect.types.notification_delivery_type
    import aws_sdk_connect.types.notification_recipient_type
    import aws_sdk_connect.types.subject


class SendNotificationActionDefinition(TypedDict):
    delivery_method: (
        "aws_sdk_connect.types.notification_delivery_type.NotificationDeliveryType"
    )
    """<p>Notification delivery method.</p>"""
    subject: NotRequired["aws_sdk_connect.types.subject.Subject"]
    r"""<p>The subject of the email if the delivery method is <code>EMAIL</code>. Supports variable injection. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html\">JSONPath reference</a> in the <i>Connect Customer Administrators Guide</i>.</p>"""
    content: "aws_sdk_connect.types.content.Content"
    r"""<p>Notification content. Supports variable injection. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html\">JSONPath reference</a> in the <i>Connect Customer Administrators Guide</i>.</p>"""
    content_type: (
        "aws_sdk_connect.types.notification_content_type.NotificationContentType"
    )
    """<p>Content type format.</p>"""
    recipient: (
        "aws_sdk_connect.types.notification_recipient_type.NotificationRecipientType"
    )
    """<p>Notification recipient.</p>"""
    exclusion: NotRequired[
        "aws_sdk_connect.types.notification_recipient_type.NotificationRecipientType"
    ]
    """<p>Recipients to exclude from notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendNotificationActionDefinition) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.notification_delivery_type

    out["DeliveryMethod"] = (
        aws_sdk_connect.types.notification_delivery_type.serialize_json(
            value["delivery_method"]
        )
    )
    if "subject" in value:
        out["Subject"] = value["subject"]
    out["Content"] = value["content"]
    import aws_sdk_connect.types.notification_content_type

    out["ContentType"] = aws_sdk_connect.types.notification_content_type.serialize_json(
        value["content_type"]
    )
    import aws_sdk_connect.types.notification_recipient_type

    out["Recipient"] = aws_sdk_connect.types.notification_recipient_type.serialize_json(
        value["recipient"]
    )
    if "exclusion" in value:
        import aws_sdk_connect.types.notification_recipient_type

        out["Exclusion"] = (
            aws_sdk_connect.types.notification_recipient_type.serialize_json(
                value["exclusion"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendNotificationActionDefinition:
    out: SendNotificationActionDefinition = {}  # type: ignore[typeddict-item]
    if "DeliveryMethod" in data:
        import aws_sdk_connect.types.notification_delivery_type

        out["delivery_method"] = (
            aws_sdk_connect.types.notification_delivery_type.deserialize_json(
                data["DeliveryMethod"]
            )
        )
    else:
        raise DeserializationError(
            "SendNotificationActionDefinition.delivery_method required"
        )
    if "Subject" in data:
        out["subject"] = data["Subject"]
    if "Content" in data:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("SendNotificationActionDefinition.content required")
    if "ContentType" in data:
        import aws_sdk_connect.types.notification_content_type

        out["content_type"] = (
            aws_sdk_connect.types.notification_content_type.deserialize_json(
                data["ContentType"]
            )
        )
    else:
        raise DeserializationError(
            "SendNotificationActionDefinition.content_type required"
        )
    if "Recipient" in data:
        import aws_sdk_connect.types.notification_recipient_type

        out["recipient"] = (
            aws_sdk_connect.types.notification_recipient_type.deserialize_json(
                data["Recipient"]
            )
        )
    else:
        raise DeserializationError(
            "SendNotificationActionDefinition.recipient required"
        )
    if "Exclusion" in data:
        import aws_sdk_connect.types.notification_recipient_type

        out["exclusion"] = (
            aws_sdk_connect.types.notification_recipient_type.deserialize_json(
                data["Exclusion"]
            )
        )
    return out
