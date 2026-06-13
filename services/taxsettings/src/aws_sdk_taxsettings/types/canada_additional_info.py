"""Generated from Smithy shape ``com.amazonaws.taxsettings#CanadaAdditionalInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.canada_provincial_sales_tax_id_string
    import aws_sdk_taxsettings.types.canada_quebec_sales_tax_number_string
    import aws_sdk_taxsettings.types.canada_retail_sales_tax_number_string


class CanadaAdditionalInfo(TypedDict):
    provincial_sales_tax_id: NotRequired[
        "aws_sdk_taxsettings.types.canada_provincial_sales_tax_id_string.CanadaProvincialSalesTaxIdString"
    ]
    """<p> The provincial sales tax ID for your TRN in Canada. This parameter can represent the following: </p> <ul> <li> <p>Provincial sales tax ID number for British Columbia and Saskatchewan provinces</p> </li> <li> <p>Manitoba retail sales tax ID number for Manitoba province</p> </li> <li> <p>Quebec sales tax ID number for Quebec province</p> </li> </ul> <p>The Tax Setting API only accepts this parameter if the TRN is specified for the previous provinces. For other provinces, the Tax Settings API doesn't accept this parameter. </p>"""
    canada_quebec_sales_tax_number: NotRequired[
        "aws_sdk_taxsettings.types.canada_quebec_sales_tax_number_string.CanadaQuebecSalesTaxNumberString"
    ]
    """<p> The Quebec Sales Tax ID number. Leave blank if you do not have a Quebec Sales Tax ID number. </p>"""
    canada_retail_sales_tax_number: NotRequired[
        "aws_sdk_taxsettings.types.canada_retail_sales_tax_number_string.CanadaRetailSalesTaxNumberString"
    ]
    """<p> Manitoba Retail Sales Tax ID number. Customers purchasing Amazon Web Services services for resale in Manitoba must provide a valid Retail Sales Tax ID number for Manitoba. Leave this blank if you do not have a Retail Sales Tax ID number in Manitoba or are not purchasing Amazon Web Services services for resale. </p>"""
    is_reseller_account: NotRequired["bool"]
    """<p> The value for this parameter must be <code>true</code> if the <code>provincialSalesTaxId</code> value is provided for a TRN in British Columbia, Saskatchewan, or Manitoba provinces. </p> <p>To claim a provincial sales tax (PST) and retail sales tax (RST) reseller exemption, you must confirm that purchases from this account were made for resale. Otherwise, remove the PST or RST number from the <code>provincialSalesTaxId</code> parameter from your request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanadaAdditionalInfo) -> dict:
    out: dict = {}
    if "provincial_sales_tax_id" in value:
        out["provincialSalesTaxId"] = value["provincial_sales_tax_id"]
    if "canada_quebec_sales_tax_number" in value:
        out["canadaQuebecSalesTaxNumber"] = value["canada_quebec_sales_tax_number"]
    if "canada_retail_sales_tax_number" in value:
        out["canadaRetailSalesTaxNumber"] = value["canada_retail_sales_tax_number"]
    if "is_reseller_account" in value:
        out["isResellerAccount"] = value["is_reseller_account"]
    return out


def deserialize_json(data: dict) -> CanadaAdditionalInfo:
    out: CanadaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "provincialSalesTaxId" in data:
        out["provincial_sales_tax_id"] = data["provincialSalesTaxId"]
    if "canadaQuebecSalesTaxNumber" in data:
        out["canada_quebec_sales_tax_number"] = data["canadaQuebecSalesTaxNumber"]
    if "canadaRetailSalesTaxNumber" in data:
        out["canada_retail_sales_tax_number"] = data["canadaRetailSalesTaxNumber"]
    if "isResellerAccount" in data:
        out["is_reseller_account"] = data["isResellerAccount"]
    return out
