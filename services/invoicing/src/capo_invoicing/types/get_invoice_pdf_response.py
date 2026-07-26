"""Generated from Smithy shape ``com.amazonaws.invoicing#GetInvoicePDFResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.invoice_pdf


class GetInvoicePDFResponse(TypedDict, closed=True):
    invoice_pdf: NotRequired["capo_invoicing.types.invoice_pdf.InvoicePDF"]
    """<p> The invoice document and supplemental documents associated with the invoice. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetInvoicePDFResponse) -> dict:
    out: dict = {}
    if "invoice_pdf" in value:
        import capo_invoicing.types.invoice_pdf

        out["InvoicePDF"] = capo_invoicing.types.invoice_pdf.serialize_aws_json_1_0(
            value["invoice_pdf"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetInvoicePDFResponse:
    out: GetInvoicePDFResponse = {}  # type: ignore[typeddict-item]
    if "InvoicePDF" in data:
        import capo_invoicing.types.invoice_pdf

        out["invoice_pdf"] = capo_invoicing.types.invoice_pdf.deserialize_aws_json_1_0(
            data["InvoicePDF"]
        )
    return out
