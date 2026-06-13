"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billing.errors import DeserializationError

BillingViewStatusReason: TypeAlias = Literal[
    "SOURCE_VIEW_UNHEALTHY",
    "SOURCE_VIEW_UPDATING",
    "SOURCE_VIEW_ACCESS_DENIED",
    "SOURCE_VIEW_NOT_FOUND",
    "CYCLIC_DEPENDENCY",
    "SOURCE_VIEW_DEPTH_EXCEEDED",
    "AGGREGATE_SOURCE",
    "VIEW_OWNER_NOT_MANAGEMENT_ACCOUNT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOURCE_VIEW_UNHEALTHY",
        "SOURCE_VIEW_UPDATING",
        "SOURCE_VIEW_ACCESS_DENIED",
        "SOURCE_VIEW_NOT_FOUND",
        "CYCLIC_DEPENDENCY",
        "SOURCE_VIEW_DEPTH_EXCEEDED",
        "AGGREGATE_SOURCE",
        "VIEW_OWNER_NOT_MANAGEMENT_ACCOUNT",
    )
)


def serialize_aws_json_1_0(value: BillingViewStatusReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingViewStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingViewStatusReason value: {data!r}")
    return cast(BillingViewStatusReason, data)
