"""Generated from Smithy shape ``com.amazonaws.connect#SlaFieldValueUnionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.field_value_union

SlaFieldValueUnionList: TypeAlias = list[
    "capo_connect.types.field_value_union.FieldValueUnion"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlaFieldValueUnionList) -> list:
    import capo_connect.types.field_value_union

    out: list = []
    for item in value:
        out.append(capo_connect.types.field_value_union.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlaFieldValueUnionList:
    import capo_connect.types.field_value_union

    out: SlaFieldValueUnionList = []
    for item in data:
        out.append(capo_connect.types.field_value_union.deserialize_json(item))
    return out
