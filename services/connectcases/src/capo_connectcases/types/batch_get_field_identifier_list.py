"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetFieldIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.field_identifier

BatchGetFieldIdentifierList: TypeAlias = list[
    "capo_connectcases.types.field_identifier.FieldIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFieldIdentifierList) -> list:
    import capo_connectcases.types.field_identifier

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.field_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetFieldIdentifierList:
    import capo_connectcases.types.field_identifier

    out: BatchGetFieldIdentifierList = []
    for item in data:
        out.append(capo_connectcases.types.field_identifier.deserialize_json(item))
    return out
