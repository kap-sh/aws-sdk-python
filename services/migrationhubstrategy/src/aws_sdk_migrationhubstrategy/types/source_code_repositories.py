"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#SourceCodeRepositories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.source_code_repository

SourceCodeRepositories: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.source_code_repository.SourceCodeRepository"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceCodeRepositories) -> list:
    import aws_sdk_migrationhubstrategy.types.source_code_repository

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhubstrategy.types.source_code_repository.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SourceCodeRepositories:
    import aws_sdk_migrationhubstrategy.types.source_code_repository

    out: SourceCodeRepositories = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.source_code_repository.deserialize_json(
                item
            )
        )
    return out
