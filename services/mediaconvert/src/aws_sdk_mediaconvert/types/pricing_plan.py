"""Generated from Smithy shape ``com.amazonaws.mediaconvert#PricingPlan``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment."""
PricingPlan: TypeAlias = Literal[
    "ON_DEMAND",
    "RESERVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DEMAND",
        "RESERVED",
    )
)


def serialize_json(value: PricingPlan) -> str:
    return value


def deserialize_json(data: str) -> PricingPlan:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PricingPlan value: {data!r}")
    return cast(PricingPlan, data)
