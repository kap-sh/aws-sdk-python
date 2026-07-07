"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateExperimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_arn


class UpdateExperimentResponse(TypedDict, closed=True):
    experiment_arn: NotRequired["aws_sdk_sagemaker.types.experiment_arn.ExperimentArn"]
    """<p>The Amazon Resource Name (ARN) of the experiment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateExperimentResponse) -> dict:
    out: dict = {}
    if "experiment_arn" in value:
        out["ExperimentArn"] = value["experiment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateExperimentResponse:
    out: UpdateExperimentResponse = {}  # type: ignore[typeddict-item]
    if "ExperimentArn" in data:
        out["experiment_arn"] = data["ExperimentArn"]
    return out
