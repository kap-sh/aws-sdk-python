"""Generated from Smithy shape ``com.amazonaws.notifications#CreateEventRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.event_rule_arn
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.status_summary_by_region


class CreateEventRuleResponse(TypedDict):
    arn: "aws_sdk_notifications.types.event_rule_arn.EventRuleArn"
    """<p>The ARN of the resource.</p>"""
    notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The ARN of a <code>NotificationConfiguration</code>.</p>"""
    status_summary_by_region: (
        "aws_sdk_notifications.types.status_summary_by_region.StatusSummaryByRegion"
    )
    """<p>A list of an <code>EventRule</code>'s status by Region. Regions are mapped to <code>EventRuleStatusSummary</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventRuleResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    import aws_sdk_notifications.types.status_summary_by_region

    out["statusSummaryByRegion"] = (
        aws_sdk_notifications.types.status_summary_by_region.serialize_json(
            value["status_summary_by_region"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateEventRuleResponse:
    out: CreateEventRuleResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateEventRuleResponse.arn required")
    if "notificationConfigurationArn" in data:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        raise DeserializationError(
            "CreateEventRuleResponse.notification_configuration_arn required"
        )
    if "statusSummaryByRegion" in data:
        import aws_sdk_notifications.types.status_summary_by_region

        out["status_summary_by_region"] = (
            aws_sdk_notifications.types.status_summary_by_region.deserialize_json(
                data["statusSummaryByRegion"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEventRuleResponse.status_summary_by_region required"
        )
    return out
