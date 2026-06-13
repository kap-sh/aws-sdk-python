"""Generated from Smithy shape ``com.amazonaws.invoicing#DeleteInvoiceUnitRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string_without_space
    import aws_sdk_invoicing.types.invoice_unit_arn_string


class DeleteInvoiceUnitRequest(TypedDict):
    invoice_unit_arn: (
        "aws_sdk_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString"
    )
    """<p> The ARN to identify an invoice unit. This information can't be modified or deleted. </p>"""
    client_token: NotRequired[
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p> A unique, case-sensitive identifier that you provide to ensure idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteInvoiceUnitRequest) -> dict:
    out: dict = {}
    out["InvoiceUnitArn"] = value["invoice_unit_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteInvoiceUnitRequest:
    out: DeleteInvoiceUnitRequest = {}  # type: ignore[typeddict-item]
    if "InvoiceUnitArn" in data:
        out["invoice_unit_arn"] = data["InvoiceUnitArn"]
    else:
        raise DeserializationError("DeleteInvoiceUnitRequest.invoice_unit_arn required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
