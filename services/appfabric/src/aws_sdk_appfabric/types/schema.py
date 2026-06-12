"""Generated from Smithy shape ``com.amazonaws.appfabric#Schema``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appfabric.errors import DeserializationError

Schema: TypeAlias = Literal[
    "ocsf",
    "raw",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ocsf",
        "raw",
    )
)


def serialize_json(value: Schema) -> str:
    return value


def deserialize_json(data: str) -> Schema:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Schema value: {data!r}")
    return cast(Schema, data)
