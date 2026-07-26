"""Generated from Smithy shape ``com.amazonaws.sagemaker#ComputeQuotaConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.compute_quota_resource_config_list
    import capo_sagemaker.types.preempt_team_tasks
    import capo_sagemaker.types.resource_sharing_config


class ComputeQuotaConfig(TypedDict, closed=True):
    compute_quota_resources: NotRequired[
        "capo_sagemaker.types.compute_quota_resource_config_list.ComputeQuotaResourceConfigList"
    ]
    """<p>Allocate compute resources by instance types.</p>"""
    resource_sharing_config: NotRequired[
        "capo_sagemaker.types.resource_sharing_config.ResourceSharingConfig"
    ]
    """<p>Resource sharing configuration. This defines how an entity can lend and borrow idle compute with other entities within the cluster.</p>"""
    preempt_team_tasks: NotRequired[
        "capo_sagemaker.types.preempt_team_tasks.PreemptTeamTasks"
    ]
    """<p>Allows workloads from within an entity to preempt same-team workloads. When set to <code>LowerPriority</code>, the entity's lower priority tasks are preempted by their own higher priority tasks.</p> <p>Default is <code>LowerPriority</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeQuotaConfig) -> dict:
    out: dict = {}
    if "compute_quota_resources" in value:
        import capo_sagemaker.types.compute_quota_resource_config_list

        out["ComputeQuotaResources"] = (
            capo_sagemaker.types.compute_quota_resource_config_list.serialize_aws_json_1_1(
                value["compute_quota_resources"]
            )
        )
    if "resource_sharing_config" in value:
        import capo_sagemaker.types.resource_sharing_config

        out["ResourceSharingConfig"] = (
            capo_sagemaker.types.resource_sharing_config.serialize_aws_json_1_1(
                value["resource_sharing_config"]
            )
        )
    if "preempt_team_tasks" in value:
        import capo_sagemaker.types.preempt_team_tasks

        out["PreemptTeamTasks"] = (
            capo_sagemaker.types.preempt_team_tasks.serialize_aws_json_1_1(
                value["preempt_team_tasks"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeQuotaConfig:
    out: ComputeQuotaConfig = {}  # type: ignore[typeddict-item]
    if "ComputeQuotaResources" in data:
        import capo_sagemaker.types.compute_quota_resource_config_list

        out["compute_quota_resources"] = (
            capo_sagemaker.types.compute_quota_resource_config_list.deserialize_aws_json_1_1(
                data["ComputeQuotaResources"]
            )
        )
    if "ResourceSharingConfig" in data:
        import capo_sagemaker.types.resource_sharing_config

        out["resource_sharing_config"] = (
            capo_sagemaker.types.resource_sharing_config.deserialize_aws_json_1_1(
                data["ResourceSharingConfig"]
            )
        )
    if "PreemptTeamTasks" in data:
        import capo_sagemaker.types.preempt_team_tasks

        out["preempt_team_tasks"] = (
            capo_sagemaker.types.preempt_team_tasks.deserialize_aws_json_1_1(
                data["PreemptTeamTasks"]
            )
        )
    return out
