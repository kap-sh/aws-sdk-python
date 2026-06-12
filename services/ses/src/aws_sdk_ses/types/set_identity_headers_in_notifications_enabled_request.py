"""Generated from Smithy shape ``com.amazonaws.ses#SetIdentityHeadersInNotificationsEnabledRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.enabled
    import aws_sdk_ses.types.identity
    import aws_sdk_ses.types.notification_type


class SetIdentityHeadersInNotificationsEnabledRequest(TypedDict):
    identity: "aws_sdk_ses.types.identity.Identity"
    """<p>The identity for which to enable or disable headers in notifications. Examples: <code>user@example.com</code>, <code>example.com</code>.</p>"""
    notification_type: "aws_sdk_ses.types.notification_type.NotificationType"
    """<p>The notification type for which to enable or disable headers in notifications. </p>"""
    enabled: "aws_sdk_ses.types.enabled.Enabled"
    """<p>Sets whether Amazon SES includes the original email headers in Amazon SNS notifications of the specified notification type. A value of <code>true</code> specifies that Amazon SES includes headers in notifications, and a value of <code>false</code> specifies that Amazon SES does not include headers in notifications.</p> <p>This value can only be set when <code>NotificationType</code> is already set to use a particular Amazon SNS topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIdentityHeadersInNotificationsEnabledRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.Identity", str(value["identity"])))
    import aws_sdk_ses.types.notification_type

    aws_sdk_ses.types.notification_type.serialize_query(
        value["notification_type"], pairs, f"{prefix}.NotificationType"
    )
    pairs.append(
        (f"{prefix}.Enabled", "true" if value.get("enabled", False) else "false")
    )


def deserialize_query(el: Element) -> SetIdentityHeadersInNotificationsEnabledRequest:
    out: SetIdentityHeadersInNotificationsEnabledRequest = {}  # type: ignore[typeddict-item]
    child_identity = el.find("Identity")
    if child_identity is not None:
        out["identity"] = str(child_identity.text or "")
    else:
        raise DeserializationError(
            "SetIdentityHeadersInNotificationsEnabledRequest.identity required"
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
            "SetIdentityHeadersInNotificationsEnabledRequest.notification_type required"
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    return out
