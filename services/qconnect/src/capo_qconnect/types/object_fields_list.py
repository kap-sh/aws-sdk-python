"""Generated from Smithy shape ``com.amazonaws.qconnect#ObjectFieldsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string

ObjectFieldsList: TypeAlias = list[
    "capo_qconnect.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectFieldsList) -> list:
    return list(value)


def deserialize_json(data: list) -> ObjectFieldsList:
    return list(data)
