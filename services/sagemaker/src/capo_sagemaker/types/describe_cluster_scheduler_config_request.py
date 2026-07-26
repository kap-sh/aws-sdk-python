"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterSchedulerConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_scheduler_config_id
    import capo_sagemaker.types.integer


class DescribeClusterSchedulerConfigRequest(TypedDict, closed=True):
    cluster_scheduler_config_id: NotRequired[
        "capo_sagemaker.types.cluster_scheduler_config_id.ClusterSchedulerConfigId"
    ]
    """<p>ID of the cluster policy.</p>"""
    cluster_scheduler_config_version: NotRequired[
        "capo_sagemaker.types.integer.Integer"
    ]
    """<p>Version of the cluster policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterSchedulerConfigRequest) -> dict:
    out: dict = {}
    if "cluster_scheduler_config_id" in value:
        out["ClusterSchedulerConfigId"] = value["cluster_scheduler_config_id"]
    if "cluster_scheduler_config_version" in value:
        out["ClusterSchedulerConfigVersion"] = value["cluster_scheduler_config_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterSchedulerConfigRequest:
    out: DescribeClusterSchedulerConfigRequest = {}  # type: ignore[typeddict-item]
    if "ClusterSchedulerConfigId" in data:
        out["cluster_scheduler_config_id"] = data["ClusterSchedulerConfigId"]
    if "ClusterSchedulerConfigVersion" in data:
        out["cluster_scheduler_config_version"] = data["ClusterSchedulerConfigVersion"]
    return out
