"""Generated from Smithy shape ``com.amazonaws.datazone#NameIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.name_identifier

NameIdentifiers: TypeAlias = list["capo_datazone.types.name_identifier.NameIdentifier"]


# --- restJson1 ser/de ---
def serialize_json(value: NameIdentifiers) -> list:
    import capo_datazone.types.name_identifier

    out: list = []
    for item in value:
        out.append(capo_datazone.types.name_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> NameIdentifiers:
    import capo_datazone.types.name_identifier

    out: NameIdentifiers = []
    for item in data:
        out.append(capo_datazone.types.name_identifier.deserialize_json(item))
    return out
