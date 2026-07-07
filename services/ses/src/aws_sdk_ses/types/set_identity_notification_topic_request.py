"""Generated from Smithy shape ``com.amazonaws.ses#SetIdentityNotificationTopicRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.identity
    import aws_sdk_ses.types.notification_topic
    import aws_sdk_ses.types.notification_type


class SetIdentityNotificationTopicRequest(TypedDict, closed=True):
    identity: "aws_sdk_ses.types.identity.Identity"
    """<p>The identity (email address or domain) for the Amazon SNS topic.</p> <important> <p>You can only specify a verified identity for this parameter.</p> </important> <p>You can specify an identity by using its name or by using its Amazon Resource Name (ARN). The following examples are all valid identities: <code>sender@example.com</code>, <code>example.com</code>, <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p>"""
    notification_type: "aws_sdk_ses.types.notification_type.NotificationType"
    """<p>The type of notifications that are published to the specified Amazon SNS topic.</p>"""
    sns_topic: NotRequired["aws_sdk_ses.types.notification_topic.NotificationTopic"]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic. If the parameter is omitted from the request or a null value is passed, <code>SnsTopic</code> is cleared and publishing is disabled.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIdentityNotificationTopicRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.Identity", str(value["identity"])))
    import aws_sdk_ses.types.notification_type

    aws_sdk_ses.types.notification_type.serialize_query(
        value["notification_type"], pairs, f"{prefix}.NotificationType"
    )
    if "sns_topic" in value:
        pairs.append((f"{prefix}.SnsTopic", str(value["sns_topic"])))


def deserialize_query(el: Element) -> SetIdentityNotificationTopicRequest:
    out: SetIdentityNotificationTopicRequest = {}  # type: ignore[typeddict-item]
    child_identity = el.find("Identity")
    if child_identity is not None:
        out["identity"] = str(child_identity.text or "")
    else:
        raise DeserializationError(
            "SetIdentityNotificationTopicRequest.identity required"
        )
    child_notification_type = el.find("NotificationType")
    if child_notification_type is not None:
        import aws_sdk_ses.types.notification_type

        out["notification_type"] = (
            aws_sdk_ses.types.notification_type.deserialize_query(
                child_notification_type
            )
        )
    else:
        raise DeserializationError(
            "SetIdentityNotificationTopicRequest.notification_type required"
        )
    child_sns_topic = el.find("SnsTopic")
    if child_sns_topic is not None:
        out["sns_topic"] = str(child_sns_topic.text or "")
    return out
