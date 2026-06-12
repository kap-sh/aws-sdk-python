"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteTrialComponentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.trial_component_arn


class DeleteTrialComponentResponse(TypedDict):
    trial_component_arn: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_arn.TrialComponentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the component is being deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTrialComponentResponse) -> dict:
    out: dict = {}
    if "trial_component_arn" in value:
        out["TrialComponentArn"] = value["trial_component_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTrialComponentResponse:
    out: DeleteTrialComponentResponse = {}  # type: ignore[typeddict-item]
    if "TrialComponentArn" in data:
        out["trial_component_arn"] = data["TrialComponentArn"]
    return out
