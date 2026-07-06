"""Generated from Smithy shape ``com.amazonaws.invoicing#UpdateInvoiceUnitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.invoice_unit_arn_string


class UpdateInvoiceUnitResponse(TypedDict, closed=True):
    invoice_unit_arn: NotRequired[
        "aws_sdk_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString"
    ]
    """<p> The ARN to identify an invoice unit. This information can't be modified or deleted. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateInvoiceUnitResponse) -> dict:
    out: dict = {}
    if "invoice_unit_arn" in value:
        out["InvoiceUnitArn"] = value["invoice_unit_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateInvoiceUnitResponse:
    out: UpdateInvoiceUnitResponse = {}  # type: ignore[typeddict-item]
    if "InvoiceUnitArn" in data:
        out["invoice_unit_arn"] = data["InvoiceUnitArn"]
    return out
