"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#MarketSegment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

MarketSegment: TypeAlias = Literal[
    "Enterprise",
    "Large",
    "Medium",
    "Small",
    "Micro",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enterprise",
        "Large",
        "Medium",
        "Small",
        "Micro",
    )
)


def serialize_aws_json_1_0(value: MarketSegment) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MarketSegment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MarketSegment value: {data!r}")
    return cast(MarketSegment, data)
