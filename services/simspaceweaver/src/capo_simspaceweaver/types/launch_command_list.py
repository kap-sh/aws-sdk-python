"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#LaunchCommandList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_simspaceweaver.types.non_empty_string

LaunchCommandList: TypeAlias = list[
    "capo_simspaceweaver.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: LaunchCommandList) -> list:
    return list(value)


def deserialize_json(data: list) -> LaunchCommandList:
    return list(data)
