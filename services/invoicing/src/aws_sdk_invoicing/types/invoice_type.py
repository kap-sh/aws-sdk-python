"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceType``."""

from typing import Literal, TypeAlias, cast

InvoiceType: TypeAlias = Literal[
    "INVOICE",
    "CREDIT_MEMO",
    "PAYMENT_RECEIPT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InvoiceType:
    return cast(InvoiceType, data)
