"""Generated from Smithy shape ``com.amazonaws.resiliencehub#FieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.field

FieldList: TypeAlias = list["capo_resiliencehub.types.field.Field"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldList) -> list:
    import capo_resiliencehub.types.field

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.field.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldList:
    import capo_resiliencehub.types.field

    out: FieldList = []
    for item in data:
        out.append(capo_resiliencehub.types.field.deserialize_json(item))
    return out
