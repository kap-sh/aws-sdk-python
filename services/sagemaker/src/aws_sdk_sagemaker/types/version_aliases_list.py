"""Generated from Smithy shape ``com.amazonaws.sagemaker#VersionAliasesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.image_version_alias_pattern

VersionAliasesList: TypeAlias = list[
    "aws_sdk_sagemaker.types.image_version_alias_pattern.ImageVersionAliasPattern"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VersionAliasesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VersionAliasesList:
    return list(data)
