"""Generated from Smithy shape ``com.amazonaws.bedrock#OfferType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

OfferType: TypeAlias = Literal[
    "ALL",
    "PUBLIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "PUBLIC",
    )
)


def serialize_json(value: OfferType) -> str:
    return value


def deserialize_json(data: str) -> OfferType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfferType value: {data!r}")
    return cast(OfferType, data)
