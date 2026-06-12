"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RepositoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.repository

RepositoryList: TypeAlias = list["aws_sdk_ecr_public.types.repository.Repository"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryList) -> list:
    import aws_sdk_ecr_public.types.repository

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr_public.types.repository.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryList:
    import aws_sdk_ecr_public.types.repository

    out: RepositoryList = []
    for item in data:
        out.append(aws_sdk_ecr_public.types.repository.deserialize_aws_json_1_1(item))
    return out
