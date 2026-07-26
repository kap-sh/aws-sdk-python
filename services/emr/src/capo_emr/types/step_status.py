"""Generated from Smithy shape ``com.amazonaws.emr#StepStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.failure_details
    import capo_emr.types.step_state
    import capo_emr.types.step_state_change_reason
    import capo_emr.types.step_timeline


class StepStatus(TypedDict, closed=True):
    state: NotRequired["capo_emr.types.step_state.StepState"]
    """<p>The execution state of the cluster step.</p>"""
    state_change_reason: NotRequired[
        "capo_emr.types.step_state_change_reason.StepStateChangeReason"
    ]
    """<p>The reason for the step execution status change.</p>"""
    failure_details: NotRequired["capo_emr.types.failure_details.FailureDetails"]
    """<p>The details for the step failure including reason, message, and log file path where the root cause was identified.</p>"""
    timeline: NotRequired["capo_emr.types.step_timeline.StepTimeline"]
    """<p>The timeline of the cluster step status over time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_emr.types.step_state

        out["State"] = capo_emr.types.step_state.serialize_aws_json_1_1(value["state"])
    if "state_change_reason" in value:
        import capo_emr.types.step_state_change_reason

        out["StateChangeReason"] = (
            capo_emr.types.step_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    if "failure_details" in value:
        import capo_emr.types.failure_details

        out["FailureDetails"] = capo_emr.types.failure_details.serialize_aws_json_1_1(
            value["failure_details"]
        )
    if "timeline" in value:
        import capo_emr.types.step_timeline

        out["Timeline"] = capo_emr.types.step_timeline.serialize_aws_json_1_1(
            value["timeline"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepStatus:
    out: StepStatus = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import capo_emr.types.step_state

        out["state"] = capo_emr.types.step_state.deserialize_aws_json_1_1(data["State"])
    if "StateChangeReason" in data:
        import capo_emr.types.step_state_change_reason

        out["state_change_reason"] = (
            capo_emr.types.step_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    if "FailureDetails" in data:
        import capo_emr.types.failure_details

        out["failure_details"] = (
            capo_emr.types.failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if "Timeline" in data:
        import capo_emr.types.step_timeline

        out["timeline"] = capo_emr.types.step_timeline.deserialize_aws_json_1_1(
            data["Timeline"]
        )
    return out
