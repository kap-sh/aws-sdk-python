"""Generated from Smithy shape ``com.amazonaws.invoicing#PurchaseOrderDataSourceType``."""

from typing import Literal, TypeAlias, cast

PurchaseOrderDataSourceType: TypeAlias = Literal[
    "ASSOCIATED_PURCHASE_ORDER_REQUIRED",
    "PURCHASE_ORDER_NOT_REQUIRED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PurchaseOrderDataSourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PurchaseOrderDataSourceType:
    return cast(PurchaseOrderDataSourceType, data)
