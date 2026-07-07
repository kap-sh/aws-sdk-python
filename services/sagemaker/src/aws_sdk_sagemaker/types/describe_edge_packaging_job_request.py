"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeEdgePackagingJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class DescribeEdgePackagingJobRequest(TypedDict, closed=True):
    edge_packaging_job_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge packaging job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEdgePackagingJobRequest) -> dict:
    out: dict = {}
    if "edge_packaging_job_name" in value:
        out["EdgePackagingJobName"] = value["edge_packaging_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEdgePackagingJobRequest:
    out: DescribeEdgePackagingJobRequest = {}  # type: ignore[typeddict-item]
    if "EdgePackagingJobName" in data:
        out["edge_packaging_job_name"] = data["EdgePackagingJobName"]
    return out
