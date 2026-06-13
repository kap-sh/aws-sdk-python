"""Generated from Smithy shape ``com.amazonaws.invoicing#DeleteInvoiceUnitResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.invoice_unit_arn_string


class DeleteInvoiceUnitResponse(TypedDict):
    invoice_unit_arn: NotRequired[
        "aws_sdk_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString"
    ]
    """<p> The ARN to identify an invoice unit. This information can't be modified or deleted. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteInvoiceUnitResponse) -> dict:
    out: dict = {}
    if "invoice_unit_arn" in value:
        out["InvoiceUnitArn"] = value["invoice_unit_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteInvoiceUnitResponse:
    out: DeleteInvoiceUnitResponse = {}  # type: ignore[typeddict-item]
    if "InvoiceUnitArn" in data:
        out["invoice_unit_arn"] = data["InvoiceUnitArn"]
    return out
