"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_name_or_arn


class DescribeClusterRequest(TypedDict, closed=True):
    cluster_name: NotRequired[
        "capo_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p>The string name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterRequest:
    out: DescribeClusterRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    return out
