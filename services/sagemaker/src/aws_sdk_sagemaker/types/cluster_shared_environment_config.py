"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSharedEnvironmentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy
    import aws_sdk_sagemaker.types.f_sx_lustre_config


class ClusterSharedEnvironmentConfig(TypedDict, closed=True):
    f_sx_lustre_deletion_policy: NotRequired[
        "aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy.ClusterFSxLustreDeletionPolicy"
    ]
    """<p>The deletion policy for the Amazon FSx for Lustre file system in the shared environment.</p>"""
    f_sx_lustre_config: NotRequired[
        "aws_sdk_sagemaker.types.f_sx_lustre_config.FSxLustreConfig"
    ]
    """<p>Configuration settings for an Amazon FSx for Lustre file system in the shared environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSharedEnvironmentConfig) -> dict:
    out: dict = {}
    if "f_sx_lustre_deletion_policy" in value:
        import aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy

        out["FSxLustreDeletionPolicy"] = (
            aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy.serialize_aws_json_1_1(
                value["f_sx_lustre_deletion_policy"]
            )
        )
    if "f_sx_lustre_config" in value:
        import aws_sdk_sagemaker.types.f_sx_lustre_config

        out["FSxLustreConfig"] = (
            aws_sdk_sagemaker.types.f_sx_lustre_config.serialize_aws_json_1_1(
                value["f_sx_lustre_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterSharedEnvironmentConfig:
    out: ClusterSharedEnvironmentConfig = {}  # type: ignore[typeddict-item]
    if "FSxLustreDeletionPolicy" in data:
        import aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy

        out["f_sx_lustre_deletion_policy"] = (
            aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy.deserialize_aws_json_1_1(
                data["FSxLustreDeletionPolicy"]
            )
        )
    if "FSxLustreConfig" in data:
        import aws_sdk_sagemaker.types.f_sx_lustre_config

        out["f_sx_lustre_config"] = (
            aws_sdk_sagemaker.types.f_sx_lustre_config.deserialize_aws_json_1_1(
                data["FSxLustreConfig"]
            )
        )
    return out
