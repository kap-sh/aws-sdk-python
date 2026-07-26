"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateTrialComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.trial_component_arn


class UpdateTrialComponentResponse(TypedDict, closed=True):
    trial_component_arn: NotRequired[
        "capo_sagemaker.types.trial_component_arn.TrialComponentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trial component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrialComponentResponse) -> dict:
    out: dict = {}
    if "trial_component_arn" in value:
        out["TrialComponentArn"] = value["trial_component_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrialComponentResponse:
    out: UpdateTrialComponentResponse = {}  # type: ignore[typeddict-item]
    if "TrialComponentArn" in data:
        out["trial_component_arn"] = data["TrialComponentArn"]
    return out
