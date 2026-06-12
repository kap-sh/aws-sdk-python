"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appfabric.errors import DeserializationError

IngestionState: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


def serialize_json(value: IngestionState) -> str:
    return value


def deserialize_json(data: str) -> IngestionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngestionState value: {data!r}")
    return cast(IngestionState, data)
