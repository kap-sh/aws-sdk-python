"""Generated from Smithy shape ``com.amazonaws.appfabric#Format``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appfabric.errors import DeserializationError

Format: TypeAlias = Literal[
    "json",
    "parquet",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "json",
        "parquet",
    )
)


def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Format value: {data!r}")
    return cast(Format, data)
