"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterNodeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_node_details


class DescribeClusterNodeResponse(TypedDict, closed=True):
    node_details: NotRequired[
        "capo_sagemaker.types.cluster_node_details.ClusterNodeDetails"
    ]
    """<p>The details of the SageMaker HyperPod cluster node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterNodeResponse) -> dict:
    out: dict = {}
    if "node_details" in value:
        import capo_sagemaker.types.cluster_node_details

        out["NodeDetails"] = (
            capo_sagemaker.types.cluster_node_details.serialize_aws_json_1_1(
                value["node_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterNodeResponse:
    out: DescribeClusterNodeResponse = {}  # type: ignore[typeddict-item]
    if "NodeDetails" in data:
        import capo_sagemaker.types.cluster_node_details

        out["node_details"] = (
            capo_sagemaker.types.cluster_node_details.deserialize_aws_json_1_1(
                data["NodeDetails"]
            )
        )
    return out
