"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateClusterSchedulerConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_scheduler_config_arn
    import capo_sagemaker.types.cluster_scheduler_config_id


class CreateClusterSchedulerConfigResponse(TypedDict, closed=True):
    cluster_scheduler_config_arn: NotRequired[
        "capo_sagemaker.types.cluster_scheduler_config_arn.ClusterSchedulerConfigArn"
    ]
    """<p>ARN of the cluster policy.</p>"""
    cluster_scheduler_config_id: NotRequired[
        "capo_sagemaker.types.cluster_scheduler_config_id.ClusterSchedulerConfigId"
    ]
    """<p>ID of the cluster policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterSchedulerConfigResponse) -> dict:
    out: dict = {}
    if "cluster_scheduler_config_arn" in value:
        out["ClusterSchedulerConfigArn"] = value["cluster_scheduler_config_arn"]
    if "cluster_scheduler_config_id" in value:
        out["ClusterSchedulerConfigId"] = value["cluster_scheduler_config_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterSchedulerConfigResponse:
    out: CreateClusterSchedulerConfigResponse = {}  # type: ignore[typeddict-item]
    if "ClusterSchedulerConfigArn" in data:
        out["cluster_scheduler_config_arn"] = data["ClusterSchedulerConfigArn"]
    if "ClusterSchedulerConfigId" in data:
        out["cluster_scheduler_config_id"] = data["ClusterSchedulerConfigId"]
    return out
