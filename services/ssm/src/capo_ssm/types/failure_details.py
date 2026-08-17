"""Generated from Smithy shape ``com.amazonaws.ssm#FailureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_parameter_map
    import capo_ssm.types.string


class FailureDetails(TypedDict, closed=True):
    failure_stage: NotRequired["capo_ssm.types.string.String"]
    """<p>The stage of the Automation execution when the failure occurred. The stages include the following: InputValidation, PreVerification, Invocation, PostVerification.</p>"""
    failure_type: NotRequired["capo_ssm.types.string.String"]
    """<p>The type of Automation failure. Failure types include the following: Action, Permission, Throttling, Verification, Internal.</p>"""
    details: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>Detailed information about the Automation step failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureDetails) -> dict:
    out: dict = {}
    if "failure_stage" in value:
        out["FailureStage"] = value["failure_stage"]
    if "failure_type" in value:
        out["FailureType"] = value["failure_type"]
    if "details" in value:
        import capo_ssm.types.automation_parameter_map

        out["Details"] = capo_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
            value["details"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailureDetails:
    out: FailureDetails = {}  # type: ignore[typeddict-item]
    if data.get("FailureStage") is not None:
        out["failure_stage"] = data["FailureStage"]
    if data.get("FailureType") is not None:
        out["failure_type"] = data["FailureType"]
    if data.get("Details") is not None:
        import capo_ssm.types.automation_parameter_map

        out["details"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Details"]
            )
        )
    return out
