"""Generated from Smithy shape ``com.amazonaws.appfabric#Schema``."""

from typing import Literal, TypeAlias, cast

Schema: TypeAlias = Literal[
    "ocsf",
    "raw",
]


# --- restJson1 ser/de ---
def serialize_json(value: Schema) -> str:
    return value


def deserialize_json(data: str) -> Schema:
    return cast(Schema, data)
