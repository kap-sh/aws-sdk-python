"""Generated from Smithy shape ``com.amazonaws.snowball#LongTermPricingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

LongTermPricingType: TypeAlias = Literal[
    "OneYear",
    "ThreeYear",
    "OneMonth",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OneYear",
        "ThreeYear",
        "OneMonth",
    )
)


def serialize_aws_json_1_1(value: LongTermPricingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LongTermPricingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LongTermPricingType value: {data!r}")
    return cast(LongTermPricingType, data)
