"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#DescribeNotificationRuleResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.created_timestamp
    import aws_sdk_codestar_notifications.types.detail_type
    import aws_sdk_codestar_notifications.types.event_type_batch
    import aws_sdk_codestar_notifications.types.last_modified_timestamp
    import aws_sdk_codestar_notifications.types.notification_rule_arn
    import aws_sdk_codestar_notifications.types.notification_rule_created_by
    import aws_sdk_codestar_notifications.types.notification_rule_name
    import aws_sdk_codestar_notifications.types.notification_rule_resource
    import aws_sdk_codestar_notifications.types.notification_rule_status
    import aws_sdk_codestar_notifications.types.tags
    import aws_sdk_codestar_notifications.types.targets_batch


class DescribeNotificationRuleResult(TypedDict):
    arn: (
        "aws_sdk_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the notification rule.</p>"""
    name: NotRequired[
        "aws_sdk_codestar_notifications.types.notification_rule_name.NotificationRuleName"
    ]
    """<p>The name of the notification rule.</p>"""
    event_types: NotRequired[
        "aws_sdk_codestar_notifications.types.event_type_batch.EventTypeBatch"
    ]
    """<p>A list of the event types associated with the notification rule.</p>"""
    resource: NotRequired[
        "aws_sdk_codestar_notifications.types.notification_rule_resource.NotificationRuleResource"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource associated with the notification rule.</p>"""
    targets: NotRequired[
        "aws_sdk_codestar_notifications.types.targets_batch.TargetsBatch"
    ]
    """<p>A list of the Amazon Q Developer in chat applications topics and Amazon Q Developer in chat applications clients associated with the notification rule.</p>"""
    detail_type: NotRequired[
        "aws_sdk_codestar_notifications.types.detail_type.DetailType"
    ]
    """<p>The level of detail included in the notifications for this resource. BASIC will include only the contents of the event as it would appear in Amazon CloudWatch. FULL will include any supplemental information provided by CodeStar Notifications and/or the service for the resource for which the notification is created.</p>"""
    created_by: NotRequired[
        "aws_sdk_codestar_notifications.types.notification_rule_created_by.NotificationRuleCreatedBy"
    ]
    """<p>The name or email alias of the person who created the notification rule.</p>"""
    status: NotRequired[
        "aws_sdk_codestar_notifications.types.notification_rule_status.NotificationRuleStatus"
    ]
    """<p>The status of the notification rule. Valid statuses are on (sending notifications) or off (not sending notifications).</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_codestar_notifications.types.created_timestamp.CreatedTimestamp"
    ]
    """<p>The date and time the notification rule was created, in timestamp format.</p>"""
    last_modified_timestamp: NotRequired[
        "aws_sdk_codestar_notifications.types.last_modified_timestamp.LastModifiedTimestamp"
    ]
    """<p>The date and time the notification rule was most recently updated, in timestamp format.</p>"""
    tags: NotRequired["aws_sdk_codestar_notifications.types.tags.Tags"]
    """<p>The tags associated with the notification rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNotificationRuleResult) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "event_types" in value:
        import aws_sdk_codestar_notifications.types.event_type_batch

        out["EventTypes"] = (
            aws_sdk_codestar_notifications.types.event_type_batch.serialize_json(
                value["event_types"]
            )
        )
    if "resource" in value:
        out["Resource"] = value["resource"]
    if "targets" in value:
        import aws_sdk_codestar_notifications.types.targets_batch

        out["Targets"] = (
            aws_sdk_codestar_notifications.types.targets_batch.serialize_json(
                value["targets"]
            )
        )
    if "detail_type" in value:
        import aws_sdk_codestar_notifications.types.detail_type

        out["DetailType"] = (
            aws_sdk_codestar_notifications.types.detail_type.serialize_json(
                value["detail_type"]
            )
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "status" in value:
        import aws_sdk_codestar_notifications.types.notification_rule_status

        out["Status"] = (
            aws_sdk_codestar_notifications.types.notification_rule_status.serialize_json(
                value["status"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_codestar_notifications.types.created_timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_codestar_notifications.types.created_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_modified_timestamp" in value:
        import aws_sdk_codestar_notifications.types.last_modified_timestamp

        out["LastModifiedTimestamp"] = (
            aws_sdk_codestar_notifications.types.last_modified_timestamp.serialize_json(
                value["last_modified_timestamp"]
            )
        )
    if "tags" in value:
        import aws_sdk_codestar_notifications.types.tags

        out["Tags"] = aws_sdk_codestar_notifications.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> DescribeNotificationRuleResult:
    out: DescribeNotificationRuleResult = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribeNotificationRuleResult.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "EventTypes" in data:
        import aws_sdk_codestar_notifications.types.event_type_batch

        out["event_types"] = (
            aws_sdk_codestar_notifications.types.event_type_batch.deserialize_json(
                data["EventTypes"]
            )
        )
    if "Resource" in data:
        out["resource"] = data["Resource"]
    if "Targets" in data:
        import aws_sdk_codestar_notifications.types.targets_batch

        out["targets"] = (
            aws_sdk_codestar_notifications.types.targets_batch.deserialize_json(
                data["Targets"]
            )
        )
    if "DetailType" in data:
        import aws_sdk_codestar_notifications.types.detail_type

        out["detail_type"] = (
            aws_sdk_codestar_notifications.types.detail_type.deserialize_json(
                data["DetailType"]
            )
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "Status" in data:
        import aws_sdk_codestar_notifications.types.notification_rule_status

        out["status"] = (
            aws_sdk_codestar_notifications.types.notification_rule_status.deserialize_json(
                data["Status"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_codestar_notifications.types.created_timestamp

        out["created_timestamp"] = (
            aws_sdk_codestar_notifications.types.created_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "LastModifiedTimestamp" in data:
        import aws_sdk_codestar_notifications.types.last_modified_timestamp

        out["last_modified_timestamp"] = (
            aws_sdk_codestar_notifications.types.last_modified_timestamp.deserialize_json(
                data["LastModifiedTimestamp"]
            )
        )
    if "Tags" in data:
        import aws_sdk_codestar_notifications.types.tags

        out["tags"] = aws_sdk_codestar_notifications.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
