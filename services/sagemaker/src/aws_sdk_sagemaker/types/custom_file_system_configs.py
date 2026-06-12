"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomFileSystemConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.custom_file_system_config

CustomFileSystemConfigs: TypeAlias = list[
    "aws_sdk_sagemaker.types.custom_file_system_config.CustomFileSystemConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomFileSystemConfigs) -> list:
    import aws_sdk_sagemaker.types.custom_file_system_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.custom_file_system_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomFileSystemConfigs:
    import aws_sdk_sagemaker.types.custom_file_system_config

    out: CustomFileSystemConfigs = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.custom_file_system_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
