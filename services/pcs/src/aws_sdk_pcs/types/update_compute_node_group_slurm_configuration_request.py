"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateComputeNodeGroupSlurmConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pcs.types.slurm_custom_settings


class UpdateComputeNodeGroupSlurmConfigurationRequest(TypedDict, closed=True):
    scale_down_idle_time_in_seconds: NotRequired["int"]
    """<p>The time (in seconds) before an idle node is scaled down. If not specified, the cluster-level setting applies. This overrides the cluster-level <code>scaleDownIdleTimeInSeconds</code> setting. A value of <code>-1</code> removes the override and applies the cluster-level setting to this compute node group. Requires Slurm version 25.11 or later.</p>"""
    slurm_custom_settings: NotRequired[
        "aws_sdk_pcs.types.slurm_custom_settings.SlurmCustomSettings"
    ]
    """<p>Additional Slurm-specific configuration that directly maps to Slurm settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: UpdateComputeNodeGroupSlurmConfigurationRequest,
) -> dict:
    out: dict = {}
    if "scale_down_idle_time_in_seconds" in value:
        out["scaleDownIdleTimeInSeconds"] = value["scale_down_idle_time_in_seconds"]
    if "slurm_custom_settings" in value:
        import aws_sdk_pcs.types.slurm_custom_settings

        out["slurmCustomSettings"] = (
            aws_sdk_pcs.types.slurm_custom_settings.serialize_aws_json_1_0(
                value["slurm_custom_settings"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateComputeNodeGroupSlurmConfigurationRequest:
    out: UpdateComputeNodeGroupSlurmConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "scaleDownIdleTimeInSeconds" in data:
        out["scale_down_idle_time_in_seconds"] = data["scaleDownIdleTimeInSeconds"]
    if "slurmCustomSettings" in data:
        import aws_sdk_pcs.types.slurm_custom_settings

        out["slurm_custom_settings"] = (
            aws_sdk_pcs.types.slurm_custom_settings.deserialize_aws_json_1_0(
                data["slurmCustomSettings"]
            )
        )
    return out
