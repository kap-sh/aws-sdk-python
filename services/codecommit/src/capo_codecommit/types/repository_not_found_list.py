"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryNotFoundList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.repository_name

RepositoryNotFoundList: TypeAlias = list[
    "capo_codecommit.types.repository_name.RepositoryName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryNotFoundList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RepositoryNotFoundList:
    return list(data)
