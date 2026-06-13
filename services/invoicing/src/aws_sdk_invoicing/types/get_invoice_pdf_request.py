"""Generated from Smithy shape ``com.amazonaws.invoicing#GetInvoicePDFRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.string_without_new_line


class GetInvoicePDFRequest(TypedDict):
    invoice_id: "aws_sdk_invoicing.types.string_without_new_line.StringWithoutNewLine"
    """<p> Your unique invoice ID. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetInvoicePDFRequest) -> dict:
    out: dict = {}
    out["InvoiceId"] = value["invoice_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetInvoicePDFRequest:
    out: GetInvoicePDFRequest = {}  # type: ignore[typeddict-item]
    if "InvoiceId" in data:
        out["invoice_id"] = data["InvoiceId"]
    else:
        raise DeserializationError("GetInvoicePDFRequest.invoice_id required")
    return out
