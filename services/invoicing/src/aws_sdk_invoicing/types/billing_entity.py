"""Generated from Smithy shape ``com.amazonaws.invoicing#BillingEntity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

BillingEntity: TypeAlias = Literal[
    "AWS",
    "AWS_MARKETPLACE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS",
        "AWS_MARKETPLACE",
    )
)


def serialize_aws_json_1_0(value: BillingEntity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingEntity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingEntity value: {data!r}")
    return cast(BillingEntity, data)
