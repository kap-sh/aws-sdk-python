"""Generated from Smithy shape ``com.amazonaws.snowball#ShippingOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

ShippingOption: TypeAlias = Literal[
    "SECOND_DAY",
    "NEXT_DAY",
    "EXPRESS",
    "STANDARD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SECOND_DAY",
        "NEXT_DAY",
        "EXPRESS",
        "STANDARD",
    )
)


def serialize_aws_json_1_1(value: ShippingOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShippingOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShippingOption value: {data!r}")
    return cast(ShippingOption, data)
