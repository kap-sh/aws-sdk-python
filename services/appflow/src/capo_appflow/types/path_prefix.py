"""Generated from Smithy shape ``com.amazonaws.appflow#PathPrefix``."""

from typing import Literal, TypeAlias, cast

PathPrefix: TypeAlias = Literal[
    "EXECUTION_ID",
    "SCHEMA_VERSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: PathPrefix) -> str:
    return value


def deserialize_json(data: str) -> PathPrefix:
    return cast(PathPrefix, data)
