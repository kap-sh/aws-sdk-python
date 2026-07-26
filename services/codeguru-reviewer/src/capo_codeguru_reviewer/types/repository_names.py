"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RepositoryNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.name

RepositoryNames: TypeAlias = list["capo_codeguru_reviewer.types.name.Name"]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryNames) -> list:
    return list(value)


def deserialize_json(data: list) -> RepositoryNames:
    return list(data)
