"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopLabelingJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.labeling_job_name


class StopLabelingJobRequest(TypedDict, closed=True):
    labeling_job_name: NotRequired[
        "capo_sagemaker.types.labeling_job_name.LabelingJobName"
    ]
    """<p>The name of the labeling job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopLabelingJobRequest) -> dict:
    out: dict = {}
    if "labeling_job_name" in value:
        out["LabelingJobName"] = value["labeling_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopLabelingJobRequest:
    out: StopLabelingJobRequest = {}  # type: ignore[typeddict-item]
    if "LabelingJobName" in data:
        out["labeling_job_name"] = data["LabelingJobName"]
    return out
