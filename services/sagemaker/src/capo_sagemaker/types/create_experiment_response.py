"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateExperimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_arn


class CreateExperimentResponse(TypedDict, closed=True):
    experiment_arn: NotRequired["capo_sagemaker.types.experiment_arn.ExperimentArn"]
    """<p>The Amazon Resource Name (ARN) of the experiment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExperimentResponse) -> dict:
    out: dict = {}
    if "experiment_arn" in value:
        out["ExperimentArn"] = value["experiment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExperimentResponse:
    out: CreateExperimentResponse = {}  # type: ignore[typeddict-item]
    if "ExperimentArn" in data:
        out["experiment_arn"] = data["ExperimentArn"]
    return out
