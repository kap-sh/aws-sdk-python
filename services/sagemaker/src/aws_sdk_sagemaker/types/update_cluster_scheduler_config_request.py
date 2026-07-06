"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateClusterSchedulerConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_scheduler_config_id
    import aws_sdk_sagemaker.types.entity_description
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.scheduler_config


class UpdateClusterSchedulerConfigRequest(TypedDict, closed=True):
    cluster_scheduler_config_id: NotRequired[
        "aws_sdk_sagemaker.types.cluster_scheduler_config_id.ClusterSchedulerConfigId"
    ]
    """<p>ID of the cluster policy.</p>"""
    target_version: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>Target version.</p>"""
    scheduler_config: NotRequired[
        "aws_sdk_sagemaker.types.scheduler_config.SchedulerConfig"
    ]
    """<p>Cluster policy configuration.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>Description of the cluster policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterSchedulerConfigRequest) -> dict:
    out: dict = {}
    if "cluster_scheduler_config_id" in value:
        out["ClusterSchedulerConfigId"] = value["cluster_scheduler_config_id"]
    if "target_version" in value:
        out["TargetVersion"] = value["target_version"]
    if "scheduler_config" in value:
        import aws_sdk_sagemaker.types.scheduler_config

        out["SchedulerConfig"] = (
            aws_sdk_sagemaker.types.scheduler_config.serialize_aws_json_1_1(
                value["scheduler_config"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterSchedulerConfigRequest:
    out: UpdateClusterSchedulerConfigRequest = {}  # type: ignore[typeddict-item]
    if "ClusterSchedulerConfigId" in data:
        out["cluster_scheduler_config_id"] = data["ClusterSchedulerConfigId"]
    if "TargetVersion" in data:
        out["target_version"] = data["TargetVersion"]
    if "SchedulerConfig" in data:
        import aws_sdk_sagemaker.types.scheduler_config

        out["scheduler_config"] = (
            aws_sdk_sagemaker.types.scheduler_config.deserialize_aws_json_1_1(
                data["SchedulerConfig"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
