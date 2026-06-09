"""Generated from Smithy shape ``com.amazonaws.dynamodb#BillingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

BillingMode: TypeAlias = Literal[
    "PROVISIONED",
    "PAY_PER_REQUEST",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONED",
        "PAY_PER_REQUEST",
    )
)


def serialize_aws_json_1_0(value: BillingMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingMode value: {data!r}")
    return cast(BillingMode, data)
