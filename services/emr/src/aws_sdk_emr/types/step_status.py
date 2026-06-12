"""Generated from Smithy shape ``com.amazonaws.emr#StepStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.failure_details
    import aws_sdk_emr.types.step_state
    import aws_sdk_emr.types.step_state_change_reason
    import aws_sdk_emr.types.step_timeline


class StepStatus(TypedDict):
    state: NotRequired["aws_sdk_emr.types.step_state.StepState"]
    """<p>The execution state of the cluster step.</p>"""
    state_change_reason: NotRequired[
        "aws_sdk_emr.types.step_state_change_reason.StepStateChangeReason"
    ]
    """<p>The reason for the step execution status change.</p>"""
    failure_details: NotRequired["aws_sdk_emr.types.failure_details.FailureDetails"]
    """<p>The details for the step failure including reason, message, and log file path where the root cause was identified.</p>"""
    timeline: NotRequired["aws_sdk_emr.types.step_timeline.StepTimeline"]
    """<p>The timeline of the cluster step status over time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_emr.types.step_state

        out["State"] = aws_sdk_emr.types.step_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_change_reason" in value:
        import aws_sdk_emr.types.step_state_change_reason

        out["StateChangeReason"] = (
            aws_sdk_emr.types.step_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    if "failure_details" in value:
        import aws_sdk_emr.types.failure_details

        out["FailureDetails"] = (
            aws_sdk_emr.types.failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    if "timeline" in value:
        import aws_sdk_emr.types.step_timeline

        out["Timeline"] = aws_sdk_emr.types.step_timeline.serialize_aws_json_1_1(
            value["timeline"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepStatus:
    out: StepStatus = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_emr.types.step_state

        out["state"] = aws_sdk_emr.types.step_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateChangeReason" in data:
        import aws_sdk_emr.types.step_state_change_reason

        out["state_change_reason"] = (
            aws_sdk_emr.types.step_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    if "FailureDetails" in data:
        import aws_sdk_emr.types.failure_details

        out["failure_details"] = (
            aws_sdk_emr.types.failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if "Timeline" in data:
        import aws_sdk_emr.types.step_timeline

        out["timeline"] = aws_sdk_emr.types.step_timeline.deserialize_aws_json_1_1(
            data["Timeline"]
        )
    return out
