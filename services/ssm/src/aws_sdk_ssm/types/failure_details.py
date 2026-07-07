"""Generated from Smithy shape ``com.amazonaws.ssm#FailureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_parameter_map
    import aws_sdk_ssm.types.string


class FailureDetails(TypedDict, closed=True):
    failure_stage: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The stage of the Automation execution when the failure occurred. The stages include the following: InputValidation, PreVerification, Invocation, PostVerification.</p>"""
    failure_type: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The type of Automation failure. Failure types include the following: Action, Permission, Throttling, Verification, Internal.</p>"""
    details: NotRequired[
        "aws_sdk_ssm.types.automation_parameter_map.AutomationParameterMap"
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
        import aws_sdk_ssm.types.automation_parameter_map

        out["Details"] = (
            aws_sdk_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailureDetails:
    out: FailureDetails = {}  # type: ignore[typeddict-item]
    if "FailureStage" in data:
        out["failure_stage"] = data["FailureStage"]
    if "FailureType" in data:
        out["failure_type"] = data["FailureType"]
    if "Details" in data:
        import aws_sdk_ssm.types.automation_parameter_map

        out["details"] = (
            aws_sdk_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Details"]
            )
        )
    return out
