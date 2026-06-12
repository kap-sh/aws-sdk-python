"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceTypeDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_type
    import aws_sdk_sagemaker.types.cluster_non_negative_instance_count
    import aws_sdk_sagemaker.types.cluster_threads_per_core


class ClusterInstanceTypeDetail(TypedDict):
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_type.ClusterInstanceType"
    ]
    """<p>The instance type.</p>"""
    current_count: NotRequired[
        "aws_sdk_sagemaker.types.cluster_non_negative_instance_count.ClusterNonNegativeInstanceCount"
    ]
    """<p>The number of instances of this type currently running in the instance group.</p>"""
    threads_per_core: NotRequired[
        "aws_sdk_sagemaker.types.cluster_threads_per_core.ClusterThreadsPerCore"
    ]
    """<p>The number of threads per CPU core for this instance type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceTypeDetail) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.cluster_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.cluster_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "current_count" in value:
        out["CurrentCount"] = value["current_count"]
    if "threads_per_core" in value:
        out["ThreadsPerCore"] = value["threads_per_core"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterInstanceTypeDetail:
    out: ClusterInstanceTypeDetail = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.cluster_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.cluster_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "CurrentCount" in data:
        out["current_count"] = data["CurrentCount"]
    if "ThreadsPerCore" in data:
        out["threads_per_core"] = data["ThreadsPerCore"]
    return out
