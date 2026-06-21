"""Generated from Smithy shape ``com.amazonaws.invoicing#ListInvoiceSummariesResourceType``."""

from typing import Literal, TypeAlias, cast

ListInvoiceSummariesResourceType: TypeAlias = Literal[
    "ACCOUNT_ID",
    "INVOICE_ID",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInvoiceSummariesResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListInvoiceSummariesResourceType:
    return cast(ListInvoiceSummariesResourceType, data)
