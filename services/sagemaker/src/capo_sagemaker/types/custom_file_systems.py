"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomFileSystems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.custom_file_system

CustomFileSystems: TypeAlias = list[
    "capo_sagemaker.types.custom_file_system.CustomFileSystem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomFileSystems) -> list:
    import capo_sagemaker.types.custom_file_system

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.custom_file_system.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CustomFileSystems:
    import capo_sagemaker.types.custom_file_system

    out: CustomFileSystems = []
    for item in data:
        out.append(
            capo_sagemaker.types.custom_file_system.deserialize_aws_json_1_1(item)
        )
    return out
