"""Generated from Smithy shape ``com.amazonaws.emr#StepStateChangeReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.step_state_change_reason_code
    import aws_sdk_emr.types.string


class StepStateChangeReason(TypedDict, closed=True):
    code: NotRequired[
        "aws_sdk_emr.types.step_state_change_reason_code.StepStateChangeReasonCode"
    ]
    """<p>The programmable code for the state change reason. Note: Currently, the service provides no code for the state change.</p>"""
    message: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The descriptive message for the state change reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepStateChangeReason) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_emr.types.step_state_change_reason_code

        out["Code"] = (
            aws_sdk_emr.types.step_state_change_reason_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StepStateChangeReason:
    out: StepStateChangeReason = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_emr.types.step_state_change_reason_code

        out["code"] = (
            aws_sdk_emr.types.step_state_change_reason_code.deserialize_aws_json_1_1(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
