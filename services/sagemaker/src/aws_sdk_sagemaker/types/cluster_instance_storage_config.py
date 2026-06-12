"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceStorageConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_ebs_volume_config
    import aws_sdk_sagemaker.types.cluster_fsx_lustre_config
    import aws_sdk_sagemaker.types.cluster_fsx_open_zfs_config


class _ClusterInstanceStorageConfig_EbsVolumeConfig(TypedDict):
    EbsVolumeConfig: (
        "aws_sdk_sagemaker.types.cluster_ebs_volume_config.ClusterEbsVolumeConfig"
    )


class _ClusterInstanceStorageConfig_FsxLustreConfig(TypedDict):
    FsxLustreConfig: (
        "aws_sdk_sagemaker.types.cluster_fsx_lustre_config.ClusterFsxLustreConfig"
    )


class _ClusterInstanceStorageConfig_FsxOpenZfsConfig(TypedDict):
    FsxOpenZfsConfig: (
        "aws_sdk_sagemaker.types.cluster_fsx_open_zfs_config.ClusterFsxOpenZfsConfig"
    )


ClusterInstanceStorageConfig: TypeAlias = (
    _ClusterInstanceStorageConfig_EbsVolumeConfig
    | _ClusterInstanceStorageConfig_FsxLustreConfig
    | _ClusterInstanceStorageConfig_FsxOpenZfsConfig
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceStorageConfig) -> dict:
    if "EbsVolumeConfig" in value:
        import aws_sdk_sagemaker.types.cluster_ebs_volume_config

        return {
            "EbsVolumeConfig": aws_sdk_sagemaker.types.cluster_ebs_volume_config.serialize_aws_json_1_1(
                value["EbsVolumeConfig"]
            )
        }
    elif "FsxLustreConfig" in value:
        import aws_sdk_sagemaker.types.cluster_fsx_lustre_config

        return {
            "FsxLustreConfig": aws_sdk_sagemaker.types.cluster_fsx_lustre_config.serialize_aws_json_1_1(
                value["FsxLustreConfig"]
            )
        }
    elif "FsxOpenZfsConfig" in value:
        import aws_sdk_sagemaker.types.cluster_fsx_open_zfs_config

        return {
            "FsxOpenZfsConfig": aws_sdk_sagemaker.types.cluster_fsx_open_zfs_config.serialize_aws_json_1_1(
                value["FsxOpenZfsConfig"]
            )
        }
    else:
        raise SerializationError("ClusterInstanceStorageConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ClusterInstanceStorageConfig:
    if "EbsVolumeConfig" in data:
        import aws_sdk_sagemaker.types.cluster_ebs_volume_config

        return {
            "EbsVolumeConfig": aws_sdk_sagemaker.types.cluster_ebs_volume_config.deserialize_aws_json_1_1(
                data["EbsVolumeConfig"]
            )
        }
    elif "FsxLustreConfig" in data:
        import aws_sdk_sagemaker.types.cluster_fsx_lustre_config

        return {
            "FsxLustreConfig": aws_sdk_sagemaker.types.cluster_fsx_lustre_config.deserialize_aws_json_1_1(
                data["FsxLustreConfig"]
            )
        }
    elif "FsxOpenZfsConfig" in data:
        import aws_sdk_sagemaker.types.cluster_fsx_open_zfs_config

        return {
            "FsxOpenZfsConfig": aws_sdk_sagemaker.types.cluster_fsx_open_zfs_config.deserialize_aws_json_1_1(
                data["FsxOpenZfsConfig"]
            )
        }
    else:
        raise DeserializationError(
            "ClusterInstanceStorageConfig: no recognized variant key"
        )
