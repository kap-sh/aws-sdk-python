"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceUnitNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.invoice_unit_name

InvoiceUnitNames: TypeAlias = list[
    "capo_invoicing.types.invoice_unit_name.InvoiceUnitName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceUnitNames) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> InvoiceUnitNames:
    return list(data)
