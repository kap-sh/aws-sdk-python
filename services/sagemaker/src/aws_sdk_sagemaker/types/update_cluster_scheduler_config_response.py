"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateClusterSchedulerConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_scheduler_config_arn
    import aws_sdk_sagemaker.types.integer


class UpdateClusterSchedulerConfigResponse(TypedDict, closed=True):
    cluster_scheduler_config_arn: NotRequired[
        "aws_sdk_sagemaker.types.cluster_scheduler_config_arn.ClusterSchedulerConfigArn"
    ]
    """<p>ARN of the cluster policy.</p>"""
    cluster_scheduler_config_version: NotRequired[
        "aws_sdk_sagemaker.types.integer.Integer"
    ]
    """<p>Version of the cluster policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterSchedulerConfigResponse) -> dict:
    out: dict = {}
    if "cluster_scheduler_config_arn" in value:
        out["ClusterSchedulerConfigArn"] = value["cluster_scheduler_config_arn"]
    if "cluster_scheduler_config_version" in value:
        out["ClusterSchedulerConfigVersion"] = value["cluster_scheduler_config_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterSchedulerConfigResponse:
    out: UpdateClusterSchedulerConfigResponse = {}  # type: ignore[typeddict-item]
    if "ClusterSchedulerConfigArn" in data:
        out["cluster_scheduler_config_arn"] = data["ClusterSchedulerConfigArn"]
    if "ClusterSchedulerConfigVersion" in data:
        out["cluster_scheduler_config_version"] = data["ClusterSchedulerConfigVersion"]
    return out
