"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomFileSystems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.custom_file_system

CustomFileSystems: TypeAlias = list[
    "aws_sdk_sagemaker.types.custom_file_system.CustomFileSystem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomFileSystems) -> list:
    import aws_sdk_sagemaker.types.custom_file_system

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.custom_file_system.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomFileSystems:
    import aws_sdk_sagemaker.types.custom_file_system

    out: CustomFileSystems = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.custom_file_system.deserialize_aws_json_1_1(item)
        )
    return out
