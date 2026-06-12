"""Generated from Smithy shape ``com.amazonaws.batch#CEType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

CEType: TypeAlias = Literal[
    "MANAGED",
    "UNMANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANAGED",
        "UNMANAGED",
    )
)


def serialize_json(value: CEType) -> str:
    return value


def deserialize_json(data: str) -> CEType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CEType value: {data!r}")
    return cast(CEType, data)
