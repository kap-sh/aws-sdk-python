"""Generated from Smithy shape ``com.amazonaws.ram#AssociatedSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.associated_source

AssociatedSourceList: TypeAlias = list[
    "capo_ram.types.associated_source.AssociatedSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedSourceList) -> list:
    import capo_ram.types.associated_source

    out: list = []
    for item in value:
        out.append(capo_ram.types.associated_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedSourceList:
    import capo_ram.types.associated_source

    out: AssociatedSourceList = []
    for item in data:
        out.append(capo_ram.types.associated_source.deserialize_json(item))
    return out
