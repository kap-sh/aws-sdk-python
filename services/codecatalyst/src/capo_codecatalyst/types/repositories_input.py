"""Generated from Smithy shape ``com.amazonaws.codecatalyst#RepositoriesInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.repository_input

RepositoriesInput: TypeAlias = list[
    "capo_codecatalyst.types.repository_input.RepositoryInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoriesInput) -> list:
    import capo_codecatalyst.types.repository_input

    out: list = []
    for item in value:
        out.append(capo_codecatalyst.types.repository_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> RepositoriesInput:
    import capo_codecatalyst.types.repository_input

    out: RepositoriesInput = []
    for item in data:
        out.append(capo_codecatalyst.types.repository_input.deserialize_json(item))
    return out
