"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.batch_get_schema_error

BatchGetSchemaErrorList: TypeAlias = list[
    "capo_cleanrooms.types.batch_get_schema_error.BatchGetSchemaError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaErrorList) -> list:
    import capo_cleanrooms.types.batch_get_schema_error

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.batch_get_schema_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetSchemaErrorList:
    import capo_cleanrooms.types.batch_get_schema_error

    out: BatchGetSchemaErrorList = []
    for item in data:
        out.append(capo_cleanrooms.types.batch_get_schema_error.deserialize_json(item))
    return out
