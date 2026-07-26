"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteTrialResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.trial_arn


class DeleteTrialResponse(TypedDict, closed=True):
    trial_arn: NotRequired["capo_sagemaker.types.trial_arn.TrialArn"]
    """<p>The Amazon Resource Name (ARN) of the trial that is being deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTrialResponse) -> dict:
    out: dict = {}
    if "trial_arn" in value:
        out["TrialArn"] = value["trial_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTrialResponse:
    out: DeleteTrialResponse = {}  # type: ignore[typeddict-item]
    if "TrialArn" in data:
        out["trial_arn"] = data["TrialArn"]
    return out
