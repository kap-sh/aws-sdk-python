"""Generated from Smithy shape ``com.amazonaws.deadline#Ec2MarketType``."""

from typing import Literal, TypeAlias, cast

Ec2MarketType: TypeAlias = Literal[
    "on-demand",
    "spot",
    "wait-and-save",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ec2MarketType) -> str:
    return value


def deserialize_json(data: str) -> Ec2MarketType:
    return cast(Ec2MarketType, data)
