"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.field_item

FieldList: TypeAlias = list["capo_connectcases.types.field_item.FieldItem"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldList) -> list:
    import capo_connectcases.types.field_item

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.field_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldList:
    import capo_connectcases.types.field_item

    out: FieldList = []
    for item in data:
        out.append(capo_connectcases.types.field_item.deserialize_json(item))
    return out
