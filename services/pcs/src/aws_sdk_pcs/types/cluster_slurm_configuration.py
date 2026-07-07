"""Generated from Smithy shape ``com.amazonaws.pcs#ClusterSlurmConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pcs.types.accounting
    import aws_sdk_pcs.types.cgroup_custom_settings
    import aws_sdk_pcs.types.jwt_auth
    import aws_sdk_pcs.types.slurm_auth_key
    import aws_sdk_pcs.types.slurm_custom_settings
    import aws_sdk_pcs.types.slurm_rest
    import aws_sdk_pcs.types.slurmdbd_custom_settings


class ClusterSlurmConfiguration(TypedDict, closed=True):
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
    auth_key: NotRequired["aws_sdk_pcs.types.slurm_auth_key.SlurmAuthKey"]
    """<p>The shared Slurm key for authentication, also known as the <b>cluster secret</b>.</p>"""
    jwt_auth: NotRequired["aws_sdk_pcs.types.jwt_auth.JwtAuth"]
    """<p>The JWT authentication configuration for Slurm REST API access.</p>"""
    accounting: NotRequired["aws_sdk_pcs.types.accounting.Accounting"]
    """<p>The accounting configuration includes configurable settings for Slurm accounting.</p>"""
    slurm_rest: NotRequired["aws_sdk_pcs.types.slurm_rest.SlurmRest"]
    """<p>The Slurm REST API configuration for the cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClusterSlurmConfiguration) -> dict:
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
    if "auth_key" in value:
        import aws_sdk_pcs.types.slurm_auth_key

        out["authKey"] = aws_sdk_pcs.types.slurm_auth_key.serialize_aws_json_1_0(
            value["auth_key"]
        )
    if "jwt_auth" in value:
        import aws_sdk_pcs.types.jwt_auth

        out["jwtAuth"] = aws_sdk_pcs.types.jwt_auth.serialize_aws_json_1_0(
            value["jwt_auth"]
        )
    if "accounting" in value:
        import aws_sdk_pcs.types.accounting

        out["accounting"] = aws_sdk_pcs.types.accounting.serialize_aws_json_1_0(
            value["accounting"]
        )
    if "slurm_rest" in value:
        import aws_sdk_pcs.types.slurm_rest

        out["slurmRest"] = aws_sdk_pcs.types.slurm_rest.serialize_aws_json_1_0(
            value["slurm_rest"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ClusterSlurmConfiguration:
    out: ClusterSlurmConfiguration = {}  # type: ignore[typeddict-item]
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
    if "authKey" in data:
        import aws_sdk_pcs.types.slurm_auth_key

        out["auth_key"] = aws_sdk_pcs.types.slurm_auth_key.deserialize_aws_json_1_0(
            data["authKey"]
        )
    if "jwtAuth" in data:
        import aws_sdk_pcs.types.jwt_auth

        out["jwt_auth"] = aws_sdk_pcs.types.jwt_auth.deserialize_aws_json_1_0(
            data["jwtAuth"]
        )
    if "accounting" in data:
        import aws_sdk_pcs.types.accounting

        out["accounting"] = aws_sdk_pcs.types.accounting.deserialize_aws_json_1_0(
            data["accounting"]
        )
    if "slurmRest" in data:
        import aws_sdk_pcs.types.slurm_rest

        out["slurm_rest"] = aws_sdk_pcs.types.slurm_rest.deserialize_aws_json_1_0(
            data["slurmRest"]
        )
    return out
