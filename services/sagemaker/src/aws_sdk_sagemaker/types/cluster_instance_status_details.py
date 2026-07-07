"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_status


class ClusterInstanceStatusDetails(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_status.ClusterInstanceStatus"
    ]
    """<p>The status of an instance in a SageMaker HyperPod cluster.</p>"""
    message: NotRequired["str"]
    """<p>The message from an instance in a SageMaker HyperPod cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceStatusDetails) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker.types.cluster_instance_status

        out["Status"] = (
            aws_sdk_sagemaker.types.cluster_instance_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterInstanceStatusDetails:
    out: ClusterInstanceStatusDetails = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker.types.cluster_instance_status

        out["status"] = (
            aws_sdk_sagemaker.types.cluster_instance_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
