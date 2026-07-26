"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.repository_name

RepositoryNameList: TypeAlias = list["capo_ecr.types.repository_name.RepositoryName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RepositoryNameList:
    return list(data)
