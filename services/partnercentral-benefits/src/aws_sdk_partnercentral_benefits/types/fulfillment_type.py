"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FulfillmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_benefits.errors import DeserializationError

FulfillmentType: TypeAlias = Literal[
    "CREDITS",
    "CASH",
    "ACCESS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREDITS",
        "CASH",
        "ACCESS",
    )
)


def serialize_aws_json_1_0(value: FulfillmentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FulfillmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FulfillmentType value: {data!r}")
    return cast(FulfillmentType, data)
