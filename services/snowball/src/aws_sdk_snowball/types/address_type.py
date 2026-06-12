"""Generated from Smithy shape ``com.amazonaws.snowball#AddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

AddressType: TypeAlias = Literal[
    "CUST_PICKUP",
    "AWS_SHIP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUST_PICKUP",
        "AWS_SHIP",
    )
)


def serialize_aws_json_1_1(value: AddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AddressType value: {data!r}")
    return cast(AddressType, data)
