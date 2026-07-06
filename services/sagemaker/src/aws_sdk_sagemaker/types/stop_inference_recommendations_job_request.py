"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopInferenceRecommendationsJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.recommendation_job_name


class StopInferenceRecommendationsJobRequest(TypedDict, closed=True):
    job_name: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_name.RecommendationJobName"
    ]
    """<p>The name of the job you want to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopInferenceRecommendationsJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopInferenceRecommendationsJobRequest:
    out: StopInferenceRecommendationsJobRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    return out
