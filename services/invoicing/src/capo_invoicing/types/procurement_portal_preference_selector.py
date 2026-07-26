"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortalPreferenceSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.invoice_unit_arns
    import capo_invoicing.types.seller_of_records


class ProcurementPortalPreferenceSelector(TypedDict, closed=True):
    invoice_unit_arns: NotRequired[
        "capo_invoicing.types.invoice_unit_arns.InvoiceUnitArns"
    ]
    """<p> The Amazon Resource Name (ARN) of invoice unit identifiers to which this preference applies. </p>"""
    seller_of_records: NotRequired[
        "capo_invoicing.types.seller_of_records.SellerOfRecords"
    ]
    """<p> The list of seller of record IDs to which this preference applies. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementPortalPreferenceSelector) -> dict:
    out: dict = {}
    if "invoice_unit_arns" in value:
        import capo_invoicing.types.invoice_unit_arns

        out["InvoiceUnitArns"] = (
            capo_invoicing.types.invoice_unit_arns.serialize_aws_json_1_0(
                value["invoice_unit_arns"]
            )
        )
    if "seller_of_records" in value:
        import capo_invoicing.types.seller_of_records

        out["SellerOfRecords"] = (
            capo_invoicing.types.seller_of_records.serialize_aws_json_1_0(
                value["seller_of_records"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProcurementPortalPreferenceSelector:
    out: ProcurementPortalPreferenceSelector = {}  # type: ignore[typeddict-item]
    if "InvoiceUnitArns" in data:
        import capo_invoicing.types.invoice_unit_arns

        out["invoice_unit_arns"] = (
            capo_invoicing.types.invoice_unit_arns.deserialize_aws_json_1_0(
                data["InvoiceUnitArns"]
            )
        )
    if "SellerOfRecords" in data:
        import capo_invoicing.types.seller_of_records

        out["seller_of_records"] = (
            capo_invoicing.types.seller_of_records.deserialize_aws_json_1_0(
                data["SellerOfRecords"]
            )
        )
    return out
