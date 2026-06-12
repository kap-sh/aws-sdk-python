"""Generated from Smithy shape ``com.amazonaws.cloudtrail#BillingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

BillingMode: TypeAlias = Literal[
    "EXTENDABLE_RETENTION_PRICING",
    "FIXED_RETENTION_PRICING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXTENDABLE_RETENTION_PRICING",
        "FIXED_RETENTION_PRICING",
    )
)


def serialize_aws_json_1_1(value: BillingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BillingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingMode value: {data!r}")
    return cast(BillingMode, data)
