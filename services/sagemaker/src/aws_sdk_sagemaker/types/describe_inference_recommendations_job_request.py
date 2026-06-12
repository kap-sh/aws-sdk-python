"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeInferenceRecommendationsJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.recommendation_job_name


class DescribeInferenceRecommendationsJobRequest(TypedDict):
    job_name: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_name.RecommendationJobName"
    ]
    """<p>The name of the job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInferenceRecommendationsJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInferenceRecommendationsJobRequest:
    out: DescribeInferenceRecommendationsJobRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    return out
