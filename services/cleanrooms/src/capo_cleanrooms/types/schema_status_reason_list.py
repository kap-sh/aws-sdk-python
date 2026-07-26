"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaStatusReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.schema_status_reason

SchemaStatusReasonList: TypeAlias = list[
    "capo_cleanrooms.types.schema_status_reason.SchemaStatusReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaStatusReasonList) -> list:
    import capo_cleanrooms.types.schema_status_reason

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.schema_status_reason.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchemaStatusReasonList:
    import capo_cleanrooms.types.schema_status_reason

    out: SchemaStatusReasonList = []
    for item in data:
        out.append(capo_cleanrooms.types.schema_status_reason.deserialize_json(item))
    return out
