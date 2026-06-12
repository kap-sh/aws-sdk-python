"""Generated from Smithy shape ``com.amazonaws.deadline#Ec2MarketType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

Ec2MarketType: TypeAlias = Literal[
    "on-demand",
    "spot",
    "wait-and-save",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "on-demand",
        "spot",
        "wait-and-save",
    )
)


def serialize_json(value: Ec2MarketType) -> str:
    return value


def deserialize_json(data: str) -> Ec2MarketType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Ec2MarketType value: {data!r}")
    return cast(Ec2MarketType, data)
