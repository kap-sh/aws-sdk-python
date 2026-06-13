"""Generated from Smithy shape ``com.amazonaws.omics#StoreType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_omics.errors import DeserializationError

StoreType: TypeAlias = Literal[
    "SEQUENCE_STORE",
    "REFERENCE_STORE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEQUENCE_STORE",
        "REFERENCE_STORE",
    )
)


def serialize_json(value: StoreType) -> str:
    return value


def deserialize_json(data: str) -> StoreType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StoreType value: {data!r}")
    return cast(StoreType, data)
