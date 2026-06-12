"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Ownership``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

Ownership: TypeAlias = Literal[
    "Self",
    "Shared",
    "Amazon",
    "ThirdParty",
    "AWSMarketplace",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Self",
        "Shared",
        "Amazon",
        "ThirdParty",
        "AWSMarketplace",
    )
)


def serialize_json(value: Ownership) -> str:
    return value


def deserialize_json(data: str) -> Ownership:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Ownership value: {data!r}")
    return cast(Ownership, data)
