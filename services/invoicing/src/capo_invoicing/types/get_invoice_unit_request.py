"""Generated from Smithy shape ``com.amazonaws.invoicing#GetInvoiceUnitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_invoicing.types.as_of_timestamp
    import capo_invoicing.types.invoice_unit_arn_string


class GetInvoiceUnitRequest(TypedDict, closed=True):
    invoice_unit_arn: (
        "capo_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString"
    )
    """<p> The ARN to identify an invoice unit. This information can't be modified or deleted. </p>"""
    as_of: NotRequired["capo_invoicing.types.as_of_timestamp.AsOfTimestamp"]
    """<p> The state of an invoice unit at a specified time. You can see legacy invoice units that are currently deleted if the <code>AsOf</code> time is set to before it was deleted. If an <code>AsOf</code> is not provided, the default value is the current time. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetInvoiceUnitRequest) -> dict:
    out: dict = {}
    out["InvoiceUnitArn"] = value["invoice_unit_arn"]
    if "as_of" in value:
        import capo_invoicing.types.as_of_timestamp

        out["AsOf"] = capo_invoicing.types.as_of_timestamp.serialize_aws_json_1_0(
            value["as_of"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetInvoiceUnitRequest:
    out: GetInvoiceUnitRequest = {}  # type: ignore[typeddict-item]
    if "InvoiceUnitArn" in data:
        out["invoice_unit_arn"] = data["InvoiceUnitArn"]
    else:
        raise DeserializationError("GetInvoiceUnitRequest.invoice_unit_arn required")
    if "AsOf" in data:
        import capo_invoicing.types.as_of_timestamp

        out["as_of"] = capo_invoicing.types.as_of_timestamp.deserialize_aws_json_1_0(
            data["AsOf"]
        )
    return out
