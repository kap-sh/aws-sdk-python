"""Generated from Smithy shape ``com.amazonaws.invoicing#ListInvoiceSummariesResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

ListInvoiceSummariesResourceType: TypeAlias = Literal[
    "ACCOUNT_ID",
    "INVOICE_ID",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT_ID",
        "INVOICE_ID",
    )
)


def serialize_aws_json_1_0(value: ListInvoiceSummariesResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListInvoiceSummariesResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListInvoiceSummariesResourceType value: {data!r}"
        )
    return cast(ListInvoiceSummariesResourceType, data)
