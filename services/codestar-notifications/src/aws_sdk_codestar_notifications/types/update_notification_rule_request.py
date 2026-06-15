"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#UpdateNotificationRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.detail_type
    import aws_sdk_codestar_notifications.types.event_type_ids
    import aws_sdk_codestar_notifications.types.notification_rule_arn
    import aws_sdk_codestar_notifications.types.notification_rule_name
    import aws_sdk_codestar_notifications.types.notification_rule_status
    import aws_sdk_codestar_notifications.types.targets


class UpdateNotificationRuleRequest(TypedDict):
    arn: (
        "aws_sdk_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the notification rule.</p>"""
    name: NotRequired[
        "aws_sdk_codestar_notifications.types.notification_rule_name.NotificationRuleName"
    ]
    """<p>The name of the notification rule.</p>"""
    status: NotRequired[
        "aws_sdk_codestar_notifications.types.notification_rule_status.NotificationRuleStatus"
    ]
    """<p>The status of the notification rule. Valid statuses include enabled (sending notifications) or disabled (not sending notifications).</p>"""
    event_type_ids: NotRequired[
        "aws_sdk_codestar_notifications.types.event_type_ids.EventTypeIds"
    ]
    r"""<p>A list of event types associated with this notification rule. For a complete list of event types and IDs, see <a href=\"https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api\">Notification concepts</a> in the <i>Developer Tools Console User Guide</i>.</p>"""
    targets: NotRequired["aws_sdk_codestar_notifications.types.targets.Targets"]
    """<p>The address and type of the targets to receive notifications from this notification rule.</p>"""
    detail_type: NotRequired[
        "aws_sdk_codestar_notifications.types.detail_type.DetailType"
    ]
    """<p>The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in Amazon CloudWatch. FULL will include any supplemental information provided by CodeStar Notifications and/or the service for the resource for which the notification is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotificationRuleRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_codestar_notifications.types.notification_rule_status

        out["Status"] = (
            aws_sdk_codestar_notifications.types.notification_rule_status.serialize_json(
                value["status"]
            )
        )
    if "event_type_ids" in value:
        import aws_sdk_codestar_notifications.types.event_type_ids

        out["EventTypeIds"] = (
            aws_sdk_codestar_notifications.types.event_type_ids.serialize_json(
                value["event_type_ids"]
            )
        )
    if "targets" in value:
        import aws_sdk_codestar_notifications.types.targets

        out["Targets"] = aws_sdk_codestar_notifications.types.targets.serialize_json(
            value["targets"]
        )
    if "detail_type" in value:
        import aws_sdk_codestar_notifications.types.detail_type

        out["DetailType"] = (
            aws_sdk_codestar_notifications.types.detail_type.serialize_json(
                value["detail_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateNotificationRuleRequest:
    out: UpdateNotificationRuleRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateNotificationRuleRequest.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_codestar_notifications.types.notification_rule_status

        out["status"] = (
            aws_sdk_codestar_notifications.types.notification_rule_status.deserialize_json(
                data["Status"]
            )
        )
    if "EventTypeIds" in data:
        import aws_sdk_codestar_notifications.types.event_type_ids

        out["event_type_ids"] = (
            aws_sdk_codestar_notifications.types.event_type_ids.deserialize_json(
                data["EventTypeIds"]
            )
        )
    if "Targets" in data:
        import aws_sdk_codestar_notifications.types.targets

        out["targets"] = aws_sdk_codestar_notifications.types.targets.deserialize_json(
            data["Targets"]
        )
    if "DetailType" in data:
        import aws_sdk_codestar_notifications.types.detail_type

        out["detail_type"] = (
            aws_sdk_codestar_notifications.types.detail_type.deserialize_json(
                data["DetailType"]
            )
        )
    return out
