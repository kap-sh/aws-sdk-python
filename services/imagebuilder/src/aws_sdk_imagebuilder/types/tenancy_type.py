"""Generated from Smithy shape ``com.amazonaws.imagebuilder#TenancyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

TenancyType: TypeAlias = Literal[
    "default",
    "dedicated",
    "host",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "dedicated",
        "host",
    )
)


def serialize_json(value: TenancyType) -> str:
    return value


def deserialize_json(data: str) -> TenancyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TenancyType value: {data!r}")
    return cast(TenancyType, data)
