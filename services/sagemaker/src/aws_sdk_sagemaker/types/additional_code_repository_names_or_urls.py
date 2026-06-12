"""Generated from Smithy shape ``com.amazonaws.sagemaker#AdditionalCodeRepositoryNamesOrUrls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.code_repository_name_or_url

AdditionalCodeRepositoryNamesOrUrls: TypeAlias = list[
    "aws_sdk_sagemaker.types.code_repository_name_or_url.CodeRepositoryNameOrUrl"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalCodeRepositoryNamesOrUrls) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AdditionalCodeRepositoryNamesOrUrls:
    return list(data)
