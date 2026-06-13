"""Generated from Smithy shape ``com.amazonaws.invoicing#PurchaseOrderDataSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

PurchaseOrderDataSourceType: TypeAlias = Literal[
    "ASSOCIATED_PURCHASE_ORDER_REQUIRED",
    "PURCHASE_ORDER_NOT_REQUIRED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSOCIATED_PURCHASE_ORDER_REQUIRED",
        "PURCHASE_ORDER_NOT_REQUIRED",
    )
)


def serialize_aws_json_1_0(value: PurchaseOrderDataSourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PurchaseOrderDataSourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PurchaseOrderDataSourceType value: {data!r}"
        )
    return cast(PurchaseOrderDataSourceType, data)
