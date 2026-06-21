"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewStatusReason``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: BillingViewStatusReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingViewStatusReason:
    return cast(BillingViewStatusReason, data)
