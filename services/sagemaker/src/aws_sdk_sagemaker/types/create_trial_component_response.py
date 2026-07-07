"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTrialComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.trial_component_arn


class CreateTrialComponentResponse(TypedDict, closed=True):
    trial_component_arn: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_arn.TrialComponentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trial component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrialComponentResponse) -> dict:
    out: dict = {}
    if "trial_component_arn" in value:
        out["TrialComponentArn"] = value["trial_component_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrialComponentResponse:
    out: CreateTrialComponentResponse = {}  # type: ignore[typeddict-item]
    if "TrialComponentArn" in data:
        out["trial_component_arn"] = data["TrialComponentArn"]
    return out
