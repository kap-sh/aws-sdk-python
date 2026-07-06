"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateClusterSoftwareResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_arn


class UpdateClusterSoftwareResponse(TypedDict, closed=True):
    cluster_arn: NotRequired["aws_sdk_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster being updated for security patching.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterSoftwareResponse) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterSoftwareResponse:
    out: UpdateClusterSoftwareResponse = {}  # type: ignore[typeddict-item]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    return out
