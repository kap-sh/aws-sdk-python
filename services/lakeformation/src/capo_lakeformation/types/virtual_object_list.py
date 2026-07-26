"""Generated from Smithy shape ``com.amazonaws.lakeformation#VirtualObjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.virtual_object

VirtualObjectList: TypeAlias = list[
    "capo_lakeformation.types.virtual_object.VirtualObject"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualObjectList) -> list:
    import capo_lakeformation.types.virtual_object

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.virtual_object.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualObjectList:
    import capo_lakeformation.types.virtual_object

    out: VirtualObjectList = []
    for item in data:
        out.append(capo_lakeformation.types.virtual_object.deserialize_json(item))
    return out
