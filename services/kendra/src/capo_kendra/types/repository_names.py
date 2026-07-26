"""Generated from Smithy shape ``com.amazonaws.kendra#RepositoryNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.repository_name

RepositoryNames: TypeAlias = list["capo_kendra.types.repository_name.RepositoryName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RepositoryNames:
    return list(data)
