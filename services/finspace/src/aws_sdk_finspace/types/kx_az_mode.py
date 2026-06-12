"""Generated from Smithy shape ``com.amazonaws.finspace#KxAzMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxAzMode: TypeAlias = Literal[
    "SINGLE",
    "MULTI",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE",
        "MULTI",
    )
)


def serialize_json(value: KxAzMode) -> str:
    return value


def deserialize_json(data: str) -> KxAzMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KxAzMode value: {data!r}")
    return cast(KxAzMode, data)
