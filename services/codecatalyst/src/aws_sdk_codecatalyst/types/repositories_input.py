"""Generated from Smithy shape ``com.amazonaws.codecatalyst#RepositoriesInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.repository_input

RepositoriesInput: TypeAlias = list[
    "aws_sdk_codecatalyst.types.repository_input.RepositoryInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoriesInput) -> list:
    import aws_sdk_codecatalyst.types.repository_input

    out: list = []
    for item in value:
        out.append(aws_sdk_codecatalyst.types.repository_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> RepositoriesInput:
    import aws_sdk_codecatalyst.types.repository_input

    out: RepositoriesInput = []
    for item in data:
        out.append(aws_sdk_codecatalyst.types.repository_input.deserialize_json(item))
    return out
