"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RepositoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr_public.types.repository

RepositoryList: TypeAlias = list["capo_ecr_public.types.repository.Repository"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryList) -> list:
    import capo_ecr_public.types.repository

    out: list = []
    for item in value:
        out.append(capo_ecr_public.types.repository.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryList:
    import capo_ecr_public.types.repository

    out: RepositoryList = []
    for item in data:
        out.append(capo_ecr_public.types.repository.deserialize_aws_json_1_1(item))
    return out
