"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationEventStep``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings
    import aws_sdk_compute_optimizer_automation.types.event_id
    import aws_sdk_compute_optimizer_automation.types.resource_id
    import aws_sdk_compute_optimizer_automation.types.step_id
    import aws_sdk_compute_optimizer_automation.types.step_status
    import aws_sdk_compute_optimizer_automation.types.step_type


class AutomationEventStep(TypedDict):
    event_id: NotRequired["aws_sdk_compute_optimizer_automation.types.event_id.EventId"]
    """<p> The ID of the automation event this step belongs to. </p>"""
    step_id: NotRequired["aws_sdk_compute_optimizer_automation.types.step_id.StepId"]
    """<p> The unique identifier for this step. </p>"""
    step_type: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.step_type.StepType"
    ]
    """<p> The type of step. </p>"""
    step_status: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.step_status.StepStatus"
    ]
    """<p> The current status of the step. </p>"""
    resource_id: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the resource being acted upon in this step.</p>"""
    start_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when this automation event step started execution.</p>"""
    completed_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when this automation event step completed execution.</p>"""
    estimated_monthly_savings: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings.EstimatedMonthlySavings"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationEventStep) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    if "step_type" in value:
        import aws_sdk_compute_optimizer_automation.types.step_type

        out["stepType"] = (
            aws_sdk_compute_optimizer_automation.types.step_type.serialize_aws_json_1_0(
                value["step_type"]
            )
        )
    if "step_status" in value:
        import aws_sdk_compute_optimizer_automation.types.step_status

        out["stepStatus"] = (
            aws_sdk_compute_optimizer_automation.types.step_status.serialize_aws_json_1_0(
                value["step_status"]
            )
        )
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "start_timestamp" in value:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["startTimestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["start_timestamp"]
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


def deserialize_aws_json_1_0(data: dict) -> AutomationEventStep:
    out: AutomationEventStep = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    if "stepType" in data:
        import aws_sdk_compute_optimizer_automation.types.step_type

        out["step_type"] = (
            aws_sdk_compute_optimizer_automation.types.step_type.deserialize_aws_json_1_0(
                data["stepType"]
            )
        )
    if "stepStatus" in data:
        import aws_sdk_compute_optimizer_automation.types.step_status

        out["step_status"] = (
            aws_sdk_compute_optimizer_automation.types.step_status.deserialize_aws_json_1_0(
                data["stepStatus"]
            )
        )
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "startTimestamp" in data:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["start_timestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startTimestamp"]
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
