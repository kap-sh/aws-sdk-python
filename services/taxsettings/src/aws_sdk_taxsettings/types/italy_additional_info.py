"""Generated from Smithy shape ``com.amazonaws.taxsettings#ItalyAdditionalInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.cig_number
    import aws_sdk_taxsettings.types.cup_number
    import aws_sdk_taxsettings.types.customer_type
    import aws_sdk_taxsettings.types.sdi_account_id
    import aws_sdk_taxsettings.types.tax_code

class ItalyAdditionalInfo(TypedDict):
    sdi_account_id: NotRequired["aws_sdk_taxsettings.types.sdi_account_id.SdiAccountId"]
    """<p> Additional tax information to specify for a TRN in Italy. Use CodiceDestinatario to receive your invoices via web service (API) or FTP. </p>"""
    cig_number: NotRequired["aws_sdk_taxsettings.types.cig_number.CigNumber"]
    """<p> The tender procedure identification code. </p>"""
    cup_number: NotRequired["aws_sdk_taxsettings.types.cup_number.CupNumber"]
    """<p> Additional tax information to specify for a TRN in Italy. This is managed by the Interministerial Committee for Economic Planning (CIPE) which characterizes every public investment project (Individual Project Code). </p>"""
    tax_code: NotRequired["aws_sdk_taxsettings.types.tax_code.TaxCode"]
    """<p>List of service tax codes for your TRN in Italy. You can use your customer tax code as part of a VAT Group. </p>"""
    customer_type: NotRequired["aws_sdk_taxsettings.types.customer_type.CustomerType"]
    """<p>The customer type for tax registration in Italy. Valid values are <code>Business</code> or <code>Individual</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ItalyAdditionalInfo) -> dict:
    out: dict = {}
    if "sdi_account_id" in value:
        out["sdiAccountId"] = value["sdi_account_id"]
    if "cig_number" in value:
        out["cigNumber"] = value["cig_number"]
    if "cup_number" in value:
        out["cupNumber"] = value["cup_number"]
    if "tax_code" in value:
        out["taxCode"] = value["tax_code"]
    if "customer_type" in value:
        import aws_sdk_taxsettings.types.customer_type
        out["customerType"] = aws_sdk_taxsettings.types.customer_type.serialize_json(value["customer_type"])
    return out


def deserialize_json(data: dict) -> ItalyAdditionalInfo:
    out: ItalyAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "sdiAccountId" in data:
        out["sdi_account_id"] = data["sdiAccountId"]
    if "cigNumber" in data:
        out["cig_number"] = data["cigNumber"]
    if "cupNumber" in data:
        out["cup_number"] = data["cupNumber"]
    if "taxCode" in data:
        out["tax_code"] = data["taxCode"]
    if "customerType" in data:
        import aws_sdk_taxsettings.types.customer_type
        out["customer_type"] = aws_sdk_taxsettings.types.customer_type.deserialize_json(data["customerType"])
    return out