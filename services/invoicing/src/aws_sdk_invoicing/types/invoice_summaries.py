"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.invoice_summary

InvoiceSummaries: TypeAlias = list[
    "aws_sdk_invoicing.types.invoice_summary.InvoiceSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceSummaries) -> list:
    import aws_sdk_invoicing.types.invoice_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_invoicing.types.invoice_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> InvoiceSummaries:
    import aws_sdk_invoicing.types.invoice_summary

    out: InvoiceSummaries = []
    for item in data:
        out.append(
            aws_sdk_invoicing.types.invoice_summary.deserialize_aws_json_1_0(item)
        )
    return out
