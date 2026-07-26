"""Generated from Smithy shape ``com.amazonaws.databrew#DatabaseOutputMode``."""

from typing import Literal, TypeAlias, cast

DatabaseOutputMode: TypeAlias = Literal["NEW_TABLE",]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseOutputMode) -> str:
    return value


def deserialize_json(data: str) -> DatabaseOutputMode:
    return cast(DatabaseOutputMode, data)
