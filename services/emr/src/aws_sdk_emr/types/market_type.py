"""Generated from Smithy shape ``com.amazonaws.emr#MarketType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

MarketType: TypeAlias = Literal[
    "ON_DEMAND",
    "SPOT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DEMAND",
        "SPOT",
    )
)


def serialize_aws_json_1_1(value: MarketType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MarketType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MarketType value: {data!r}")
    return cast(MarketType, data)
