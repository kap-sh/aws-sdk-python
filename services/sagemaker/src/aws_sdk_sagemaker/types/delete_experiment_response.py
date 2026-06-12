"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteExperimentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_arn


class DeleteExperimentResponse(TypedDict):
    experiment_arn: NotRequired["aws_sdk_sagemaker.types.experiment_arn.ExperimentArn"]
    """<p>The Amazon Resource Name (ARN) of the experiment that is being deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteExperimentResponse) -> dict:
    out: dict = {}
    if "experiment_arn" in value:
        out["ExperimentArn"] = value["experiment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteExperimentResponse:
    out: DeleteExperimentResponse = {}  # type: ignore[typeddict-item]
    if "ExperimentArn" in data:
        out["experiment_arn"] = data["ExperimentArn"]
    return out
