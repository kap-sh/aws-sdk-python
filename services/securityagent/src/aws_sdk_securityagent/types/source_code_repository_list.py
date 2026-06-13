"""Generated from Smithy shape ``com.amazonaws.securityagent#SourceCodeRepositoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.source_code_repository

SourceCodeRepositoryList: TypeAlias = list[
    "aws_sdk_securityagent.types.source_code_repository.SourceCodeRepository"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceCodeRepositoryList) -> list:
    import aws_sdk_securityagent.types.source_code_repository

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityagent.types.source_code_repository.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SourceCodeRepositoryList:
    import aws_sdk_securityagent.types.source_code_repository

    out: SourceCodeRepositoryList = []
    for item in data:
        out.append(
            aws_sdk_securityagent.types.source_code_repository.deserialize_json(item)
        )
    return out
