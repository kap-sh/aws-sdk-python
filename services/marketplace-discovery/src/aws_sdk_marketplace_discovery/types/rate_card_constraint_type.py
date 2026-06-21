"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#RateCardConstraintType``."""

from typing import Literal, TypeAlias, cast

RateCardConstraintType: TypeAlias = Literal[
    "Allowed",
    "Disallowed",
]


# --- restJson1 ser/de ---
def serialize_json(value: RateCardConstraintType) -> str:
    return value


def deserialize_json(data: str) -> RateCardConstraintType:
    return cast(RateCardConstraintType, data)
