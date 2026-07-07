"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSharedEnvironmentConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy
    import aws_sdk_sagemaker.types.f_sx_lustre_config


class ClusterSharedEnvironmentConfigDetails(TypedDict, closed=True):
    current_f_sx_lustre_config: NotRequired[
        "aws_sdk_sagemaker.types.f_sx_lustre_config.FSxLustreConfig"
    ]
    """<p>The current Amazon FSx for Lustre file system configuration in the shared environment.</p>"""
    desired_f_sx_lustre_config: NotRequired[
        "aws_sdk_sagemaker.types.f_sx_lustre_config.FSxLustreConfig"
    ]
    """<p>The desired Amazon FSx for Lustre file system configuration in the shared environment.</p>"""
    current_f_sx_lustre_deletion_policy: NotRequired[
        "aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy.ClusterFSxLustreDeletionPolicy"
    ]
    """<p>The current deletion policy for the Amazon FSx for Lustre file system in the shared environment.</p>"""
    desired_f_sx_lustre_deletion_policy: NotRequired[
        "aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy.ClusterFSxLustreDeletionPolicy"
    ]
    """<p>The desired deletion policy for the Amazon FSx for Lustre file system in the shared environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSharedEnvironmentConfigDetails) -> dict:
    out: dict = {}
    if "current_f_sx_lustre_config" in value:
        import aws_sdk_sagemaker.types.f_sx_lustre_config

        out["CurrentFSxLustreConfig"] = (
            aws_sdk_sagemaker.types.f_sx_lustre_config.serialize_aws_json_1_1(
                value["current_f_sx_lustre_config"]
            )
        )
    if "desired_f_sx_lustre_config" in value:
        import aws_sdk_sagemaker.types.f_sx_lustre_config

        out["DesiredFSxLustreConfig"] = (
            aws_sdk_sagemaker.types.f_sx_lustre_config.serialize_aws_json_1_1(
                value["desired_f_sx_lustre_config"]
            )
        )
    if "current_f_sx_lustre_deletion_policy" in value:
        import aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy

        out["CurrentFSxLustreDeletionPolicy"] = (
            aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy.serialize_aws_json_1_1(
                value["current_f_sx_lustre_deletion_policy"]
            )
        )
    if "desired_f_sx_lustre_deletion_policy" in value:
        import aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy

        out["DesiredFSxLustreDeletionPolicy"] = (
            aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy.serialize_aws_json_1_1(
                value["desired_f_sx_lustre_deletion_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterSharedEnvironmentConfigDetails:
    out: ClusterSharedEnvironmentConfigDetails = {}  # type: ignore[typeddict-item]
    if "CurrentFSxLustreConfig" in data:
        import aws_sdk_sagemaker.types.f_sx_lustre_config

        out["current_f_sx_lustre_config"] = (
            aws_sdk_sagemaker.types.f_sx_lustre_config.deserialize_aws_json_1_1(
                data["CurrentFSxLustreConfig"]
            )
        )
    if "DesiredFSxLustreConfig" in data:
        import aws_sdk_sagemaker.types.f_sx_lustre_config

        out["desired_f_sx_lustre_config"] = (
            aws_sdk_sagemaker.types.f_sx_lustre_config.deserialize_aws_json_1_1(
                data["DesiredFSxLustreConfig"]
            )
        )
    if "CurrentFSxLustreDeletionPolicy" in data:
        import aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy

        out["current_f_sx_lustre_deletion_policy"] = (
            aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy.deserialize_aws_json_1_1(
                data["CurrentFSxLustreDeletionPolicy"]
            )
        )
    if "DesiredFSxLustreDeletionPolicy" in data:
        import aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy

        out["desired_f_sx_lustre_deletion_policy"] = (
            aws_sdk_sagemaker.types.cluster_f_sx_lustre_deletion_policy.deserialize_aws_json_1_1(
                data["DesiredFSxLustreDeletionPolicy"]
            )
        )
    return out
