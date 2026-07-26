"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.field_value

FieldValueList: TypeAlias = list["capo_connectcases.types.field_value.FieldValue"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldValueList) -> list:
    import capo_connectcases.types.field_value

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.field_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldValueList:
    import capo_connectcases.types.field_value

    out: FieldValueList = []
    for item in data:
        out.append(capo_connectcases.types.field_value.deserialize_json(item))
    return out
