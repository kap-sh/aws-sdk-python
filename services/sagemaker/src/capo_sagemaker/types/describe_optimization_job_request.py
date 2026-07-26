"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeOptimizationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name


class DescribeOptimizationJobRequest(TypedDict, closed=True):
    optimization_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name that you assigned to the optimization job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOptimizationJobRequest) -> dict:
    out: dict = {}
    if "optimization_job_name" in value:
        out["OptimizationJobName"] = value["optimization_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeOptimizationJobRequest:
    out: DescribeOptimizationJobRequest = {}  # type: ignore[typeddict-item]
    if "OptimizationJobName" in data:
        out["optimization_job_name"] = data["OptimizationJobName"]
    return out
