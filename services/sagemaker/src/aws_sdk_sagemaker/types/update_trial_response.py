"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateTrialResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.trial_arn


class UpdateTrialResponse(TypedDict):
    trial_arn: NotRequired["aws_sdk_sagemaker.types.trial_arn.TrialArn"]
    """<p>The Amazon Resource Name (ARN) of the trial.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrialResponse) -> dict:
    out: dict = {}
    if "trial_arn" in value:
        out["TrialArn"] = value["trial_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrialResponse:
    out: UpdateTrialResponse = {}  # type: ignore[typeddict-item]
    if "TrialArn" in data:
        out["trial_arn"] = data["TrialArn"]
    return out
