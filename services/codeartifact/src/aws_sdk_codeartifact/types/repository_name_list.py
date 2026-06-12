"""Generated from Smithy shape ``com.amazonaws.codeartifact#RepositoryNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.repository_name

RepositoryNameList: TypeAlias = list[
    "aws_sdk_codeartifact.types.repository_name.RepositoryName"
]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> RepositoryNameList:
    return list(data)
