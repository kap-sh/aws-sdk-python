"""Generated from Smithy shape ``com.amazonaws.medialive#InputSdiSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.__string

InputSdiSources: TypeAlias = list["capo_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: InputSdiSources) -> list:
    return list(value)


def deserialize_json(data: list) -> InputSdiSources:
    return list(data)
