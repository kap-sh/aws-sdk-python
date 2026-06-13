"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_compute_optimizer_automation.types.account_id
    import aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings
    import aws_sdk_compute_optimizer_automation.types.event_id
    import aws_sdk_compute_optimizer_automation.types.event_status
    import aws_sdk_compute_optimizer_automation.types.event_type
    import aws_sdk_compute_optimizer_automation.types.recommended_action_id
    import aws_sdk_compute_optimizer_automation.types.resource_arn
    import aws_sdk_compute_optimizer_automation.types.resource_id
    import aws_sdk_compute_optimizer_automation.types.resource_type
    import aws_sdk_compute_optimizer_automation.types.rule_id


class AutomationEvent(TypedDict):
    event_id: NotRequired["aws_sdk_compute_optimizer_automation.types.event_id.EventId"]
    """<p> The unique identifier for the automation event. </p>"""
    event_description: NotRequired["str"]
    """<p> A description of the automation event. </p>"""
    event_type: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.event_type.EventType"
    ]
    """<p> The type of automation event. </p>"""
    event_status: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.event_status.EventStatus"
    ]
    """<p> The current status of the automation event. </p>"""
    event_status_reason: NotRequired["str"]
    """<p> The reason for the current event status. </p>"""
    resource_arn: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.resource_arn.ResourceArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the resource affected by the automation event. </p>"""
    resource_id: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.resource_id.ResourceId"
    ]
    """<p> The ID of the resource affected by the automation event. </p>"""
    recommended_action_id: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.recommended_action_id.RecommendedActionId"
    ]
    """<p> The ID of the recommended action associated with this automation event. </p>"""
    account_id: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.account_id.AccountId"
    ]
    """<p> The Amazon Web Services account ID associated with the automation event. </p>"""
    region: NotRequired["str"]
    """<p> The Amazon Web Services Region where the automation event occurred. </p>"""
    rule_id: NotRequired["aws_sdk_compute_optimizer_automation.types.rule_id.RuleId"]
    """<p> The ID of the automation rule that triggered this event. </p>"""
    resource_type: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.resource_type.ResourceType"
    ]
    """<p> The type of resource affected by the automation event. </p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the automation event was created.</p>"""
    completed_timestamp: NotRequired["datetime.datetime"]
    """<p> The timestamp when the automation event completed. </p>"""
    estimated_monthly_savings: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings.EstimatedMonthlySavings"
    ]
    """<p> The estimated monthly cost savings associated with this automation event. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationEvent) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_description" in value:
        out["eventDescription"] = value["event_description"]
    if "event_type" in value:
        import aws_sdk_compute_optimizer_automation.types.event_type

        out["eventType"] = (
            aws_sdk_compute_optimizer_automation.types.event_type.serialize_aws_json_1_0(
                value["event_type"]
            )
        )
    if "event_status" in value:
        import aws_sdk_compute_optimizer_automation.types.event_status

        out["eventStatus"] = (
            aws_sdk_compute_optimizer_automation.types.event_status.serialize_aws_json_1_0(
                value["event_status"]
            )
        )
    if "event_status_reason" in value:
        out["eventStatusReason"] = value["event_status_reason"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "recommended_action_id" in value:
        out["recommendedActionId"] = value["recommended_action_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "resource_type" in value:
        import aws_sdk_compute_optimizer_automation.types.resource_type

        out["resourceType"] = (
            aws_sdk_compute_optimizer_automation.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["createdTimestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    if "completed_timestamp" in value:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["completedTimestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["completed_timestamp"]
            )
        )
    if "estimated_monthly_savings" in value:
        import aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings.serialize_aws_json_1_0(
                value["estimated_monthly_savings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutomationEvent:
    out: AutomationEvent = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "eventDescription" in data:
        out["event_description"] = data["eventDescription"]
    if "eventType" in data:
        import aws_sdk_compute_optimizer_automation.types.event_type

        out["event_type"] = (
            aws_sdk_compute_optimizer_automation.types.event_type.deserialize_aws_json_1_0(
                data["eventType"]
            )
        )
    if "eventStatus" in data:
        import aws_sdk_compute_optimizer_automation.types.event_status

        out["event_status"] = (
            aws_sdk_compute_optimizer_automation.types.event_status.deserialize_aws_json_1_0(
                data["eventStatus"]
            )
        )
    if "eventStatusReason" in data:
        out["event_status_reason"] = data["eventStatusReason"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "recommendedActionId" in data:
        out["recommended_action_id"] = data["recommendedActionId"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "region" in data:
        out["region"] = data["region"]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    if "resourceType" in data:
        import aws_sdk_compute_optimizer_automation.types.resource_type

        out["resource_type"] = (
            aws_sdk_compute_optimizer_automation.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    if "createdTimestamp" in data:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdTimestamp"]
            )
        )
    if "completedTimestamp" in data:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["completed_timestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["completedTimestamp"]
            )
        )
    if "estimatedMonthlySavings" in data:
        import aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    return out
