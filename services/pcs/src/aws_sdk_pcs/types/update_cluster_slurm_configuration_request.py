"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateClusterSlurmConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pcs.types.cgroup_custom_settings
    import aws_sdk_pcs.types.slurm_custom_settings
    import aws_sdk_pcs.types.slurmdbd_custom_settings
    import aws_sdk_pcs.types.update_accounting_request
    import aws_sdk_pcs.types.update_slurm_rest_request


class UpdateClusterSlurmConfigurationRequest(TypedDict):
    scale_down_idle_time_in_seconds: NotRequired["int"]
    """<p>The time (in seconds) before an idle node is scaled down.</p> <p>Default: <code>600</code> </p>"""
    slurm_custom_settings: NotRequired[
        "aws_sdk_pcs.types.slurm_custom_settings.SlurmCustomSettings"
    ]
    """<p>Additional Slurm-specific configuration that directly maps to Slurm settings.</p>"""
    slurmdbd_custom_settings: NotRequired[
        "aws_sdk_pcs.types.slurmdbd_custom_settings.SlurmdbdCustomSettings"
    ]
    """<p>Additional SlurmDBD-specific configuration that directly maps to SlurmDBD settings.</p>"""
    cgroup_custom_settings: NotRequired[
        "aws_sdk_pcs.types.cgroup_custom_settings.CgroupCustomSettings"
    ]
    """<p>Additional Cgroup-specific configuration that directly maps to Cgroup settings.</p>"""
    accounting: NotRequired[
        "aws_sdk_pcs.types.update_accounting_request.UpdateAccountingRequest"
    ]
    """<p>The accounting configuration includes configurable settings for Slurm accounting.</p>"""
    slurm_rest: NotRequired[
        "aws_sdk_pcs.types.update_slurm_rest_request.UpdateSlurmRestRequest"
    ]
    """<p>The Slurm REST API configuration for the cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateClusterSlurmConfigurationRequest) -> dict:
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
    if "slurmdbd_custom_settings" in value:
        import aws_sdk_pcs.types.slurmdbd_custom_settings

        out["slurmdbdCustomSettings"] = (
            aws_sdk_pcs.types.slurmdbd_custom_settings.serialize_aws_json_1_0(
                value["slurmdbd_custom_settings"]
            )
        )
    if "cgroup_custom_settings" in value:
        import aws_sdk_pcs.types.cgroup_custom_settings

        out["cgroupCustomSettings"] = (
            aws_sdk_pcs.types.cgroup_custom_settings.serialize_aws_json_1_0(
                value["cgroup_custom_settings"]
            )
        )
    if "accounting" in value:
        import aws_sdk_pcs.types.update_accounting_request

        out["accounting"] = (
            aws_sdk_pcs.types.update_accounting_request.serialize_aws_json_1_0(
                value["accounting"]
            )
        )
    if "slurm_rest" in value:
        import aws_sdk_pcs.types.update_slurm_rest_request

        out["slurmRest"] = (
            aws_sdk_pcs.types.update_slurm_rest_request.serialize_aws_json_1_0(
                value["slurm_rest"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateClusterSlurmConfigurationRequest:
    out: UpdateClusterSlurmConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "scaleDownIdleTimeInSeconds" in data:
        out["scale_down_idle_time_in_seconds"] = data["scaleDownIdleTimeInSeconds"]
    if "slurmCustomSettings" in data:
        import aws_sdk_pcs.types.slurm_custom_settings

        out["slurm_custom_settings"] = (
            aws_sdk_pcs.types.slurm_custom_settings.deserialize_aws_json_1_0(
                data["slurmCustomSettings"]
            )
        )
    if "slurmdbdCustomSettings" in data:
        import aws_sdk_pcs.types.slurmdbd_custom_settings

        out["slurmdbd_custom_settings"] = (
            aws_sdk_pcs.types.slurmdbd_custom_settings.deserialize_aws_json_1_0(
                data["slurmdbdCustomSettings"]
            )
        )
    if "cgroupCustomSettings" in data:
        import aws_sdk_pcs.types.cgroup_custom_settings

        out["cgroup_custom_settings"] = (
            aws_sdk_pcs.types.cgroup_custom_settings.deserialize_aws_json_1_0(
                data["cgroupCustomSettings"]
            )
        )
    if "accounting" in data:
        import aws_sdk_pcs.types.update_accounting_request

        out["accounting"] = (
            aws_sdk_pcs.types.update_accounting_request.deserialize_aws_json_1_0(
                data["accounting"]
            )
        )
    if "slurmRest" in data:
        import aws_sdk_pcs.types.update_slurm_rest_request

        out["slurm_rest"] = (
            aws_sdk_pcs.types.update_slurm_rest_request.deserialize_aws_json_1_0(
                data["slurmRest"]
            )
        )
    return out
