"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceUnits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.invoice_unit

InvoiceUnits: TypeAlias = list["capo_invoicing.types.invoice_unit.InvoiceUnit"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceUnits) -> list:
    import capo_invoicing.types.invoice_unit

    out: list = []
    for item in value:
        out.append(capo_invoicing.types.invoice_unit.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> InvoiceUnits:
    import capo_invoicing.types.invoice_unit

    out: InvoiceUnits = []
    for item in data:
        out.append(capo_invoicing.types.invoice_unit.deserialize_aws_json_1_0(item))
    return out
