"""Generated from Smithy shape ``com.amazonaws.datazone#GlueConnectionNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.glue_connection_name

GlueConnectionNames: TypeAlias = list[
    "capo_datazone.types.glue_connection_name.GlueConnectionName"
]


# --- restJson1 ser/de ---
def serialize_json(value: GlueConnectionNames) -> list:
    return list(value)


def deserialize_json(data: list) -> GlueConnectionNames:
    return list(data)
