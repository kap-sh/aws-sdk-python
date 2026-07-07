"""Generated from Smithy shape ``com.amazonaws.sagemaker#DisassociateTrialComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.trial_arn
    import aws_sdk_sagemaker.types.trial_component_arn


class DisassociateTrialComponentResponse(TypedDict, closed=True):
    trial_component_arn: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_arn.TrialComponentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trial component.</p>"""
    trial_arn: NotRequired["aws_sdk_sagemaker.types.trial_arn.TrialArn"]
    """<p>The Amazon Resource Name (ARN) of the trial.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateTrialComponentResponse) -> dict:
    out: dict = {}
    if "trial_component_arn" in value:
        out["TrialComponentArn"] = value["trial_component_arn"]
    if "trial_arn" in value:
        out["TrialArn"] = value["trial_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateTrialComponentResponse:
    out: DisassociateTrialComponentResponse = {}  # type: ignore[typeddict-item]
    if "TrialComponentArn" in data:
        out["trial_component_arn"] = data["TrialComponentArn"]
    if "TrialArn" in data:
        out["trial_arn"] = data["TrialArn"]
    return out
