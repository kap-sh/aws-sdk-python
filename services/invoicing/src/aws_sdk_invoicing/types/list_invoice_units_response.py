"""Generated from Smithy shape ``com.amazonaws.invoicing#ListInvoiceUnitsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.invoice_units
    import aws_sdk_invoicing.types.next_token_string


class ListInvoiceUnitsResponse(TypedDict):
    invoice_units: NotRequired["aws_sdk_invoicing.types.invoice_units.InvoiceUnits"]
    """<p> An invoice unit is a set of mutually exclusive accounts that correspond to your business entity. </p>"""
    next_token: NotRequired["aws_sdk_invoicing.types.next_token_string.NextTokenString"]
    """<p>The next token used to indicate where the returned list should start from. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInvoiceUnitsResponse) -> dict:
    out: dict = {}
    if "invoice_units" in value:
        import aws_sdk_invoicing.types.invoice_units

        out["InvoiceUnits"] = (
            aws_sdk_invoicing.types.invoice_units.serialize_aws_json_1_0(
                value["invoice_units"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInvoiceUnitsResponse:
    out: ListInvoiceUnitsResponse = {}  # type: ignore[typeddict-item]
    if "InvoiceUnits" in data:
        import aws_sdk_invoicing.types.invoice_units

        out["invoice_units"] = (
            aws_sdk_invoicing.types.invoice_units.deserialize_aws_json_1_0(
                data["InvoiceUnits"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
