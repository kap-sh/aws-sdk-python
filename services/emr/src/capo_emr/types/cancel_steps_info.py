"""Generated from Smithy shape ``com.amazonaws.emr#CancelStepsInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.cancel_steps_request_status
    import capo_emr.types.step_id
    import capo_emr.types.string


class CancelStepsInfo(TypedDict, closed=True):
    step_id: NotRequired["capo_emr.types.step_id.StepId"]
    """<p>The encrypted StepId of a step.</p>"""
    status: NotRequired[
        "capo_emr.types.cancel_steps_request_status.CancelStepsRequestStatus"
    ]
    """<p>The status of a CancelSteps Request. The value may be SUBMITTED or FAILED.</p>"""
    reason: NotRequired["capo_emr.types.string.String"]
    """<p>The reason for the failure if the CancelSteps request fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelStepsInfo) -> dict:
    out: dict = {}
    if "step_id" in value:
        out["StepId"] = value["step_id"]
    if "status" in value:
        import capo_emr.types.cancel_steps_request_status

        out["Status"] = (
            capo_emr.types.cancel_steps_request_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelStepsInfo:
    out: CancelStepsInfo = {}  # type: ignore[typeddict-item]
    if "StepId" in data:
        out["step_id"] = data["StepId"]
    if "Status" in data:
        import capo_emr.types.cancel_steps_request_status

        out["status"] = (
            capo_emr.types.cancel_steps_request_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
