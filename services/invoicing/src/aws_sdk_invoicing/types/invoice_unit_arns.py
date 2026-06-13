"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceUnitArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.invoice_unit_arn_string

InvoiceUnitArns: TypeAlias = list[
    "aws_sdk_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceUnitArns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> InvoiceUnitArns:
    return list(data)
