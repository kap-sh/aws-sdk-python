"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_category
    import aws_sdk_sagemaker.types.job_name


class StopJobRequest(TypedDict, closed=True):
    job_name: NotRequired["aws_sdk_sagemaker.types.job_name.JobName"]
    """<p>The name of the job to stop.</p>"""
    job_category: NotRequired["aws_sdk_sagemaker.types.job_category.JobCategory"]
    """<p>The category of the job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_category" in value:
        import aws_sdk_sagemaker.types.job_category

        out["JobCategory"] = (
            aws_sdk_sagemaker.types.job_category.serialize_aws_json_1_1(
                value["job_category"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopJobRequest:
    out: StopJobRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobCategory" in data:
        import aws_sdk_sagemaker.types.job_category

        out["job_category"] = (
            aws_sdk_sagemaker.types.job_category.deserialize_aws_json_1_1(
                data["JobCategory"]
            )
        )
    return out
