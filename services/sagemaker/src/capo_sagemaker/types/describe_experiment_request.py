"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeExperimentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name


class DescribeExperimentRequest(TypedDict, closed=True):
    experiment_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExperimentRequest) -> dict:
    out: dict = {}
    if "experiment_name" in value:
        out["ExperimentName"] = value["experiment_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExperimentRequest:
    out: DescribeExperimentRequest = {}  # type: ignore[typeddict-item]
    if "ExperimentName" in data:
        out["experiment_name"] = data["ExperimentName"]
    return out
