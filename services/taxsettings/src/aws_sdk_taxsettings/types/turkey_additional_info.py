"""Generated from Smithy shape ``com.amazonaws.taxsettings#TurkeyAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.industries
    import aws_sdk_taxsettings.types.kep_email_id
    import aws_sdk_taxsettings.types.secondary_tax_id
    import aws_sdk_taxsettings.types.tax_office


class TurkeyAdditionalInfo(TypedDict, closed=True):
    tax_office: NotRequired["aws_sdk_taxsettings.types.tax_office.TaxOffice"]
    """<p>The tax office where you're registered. You can enter this information as a string. The Tax Settings API will add this information to your invoice. This parameter is required for business-to-business (B2B) and business-to-government customers. It's not required for business-to-consumer (B2C) customers.</p>"""
    kep_email_id: NotRequired["aws_sdk_taxsettings.types.kep_email_id.KepEmailId"]
    """<p>The Registered Electronic Mail (REM) that is used to send notarized communication. This parameter is optional for business-to-business (B2B) and business-to-government (B2G) customers. It's not required for business-to-consumer (B2C) customers.</p>"""
    secondary_tax_id: NotRequired[
        "aws_sdk_taxsettings.types.secondary_tax_id.SecondaryTaxId"
    ]
    """<p> Secondary tax ID (“harcama birimi VKN”si”). If one isn't provided, we will use your VKN as the secondary ID. </p>"""
    industries: NotRequired["aws_sdk_taxsettings.types.industries.Industries"]
    """<p>The industry information that tells the Tax Settings API if you're subject to additional withholding taxes. This information required for business-to-business (B2B) customers. This information is conditionally mandatory for B2B customers who are subject to KDV tax.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TurkeyAdditionalInfo) -> dict:
    out: dict = {}
    if "tax_office" in value:
        out["taxOffice"] = value["tax_office"]
    if "kep_email_id" in value:
        out["kepEmailId"] = value["kep_email_id"]
    if "secondary_tax_id" in value:
        out["secondaryTaxId"] = value["secondary_tax_id"]
    if "industries" in value:
        import aws_sdk_taxsettings.types.industries

        out["industries"] = aws_sdk_taxsettings.types.industries.serialize_json(
            value["industries"]
        )
    return out


def deserialize_json(data: dict) -> TurkeyAdditionalInfo:
    out: TurkeyAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "taxOffice" in data:
        out["tax_office"] = data["taxOffice"]
    if "kepEmailId" in data:
        out["kep_email_id"] = data["kepEmailId"]
    if "secondaryTaxId" in data:
        out["secondary_tax_id"] = data["secondaryTaxId"]
    if "industries" in data:
        import aws_sdk_taxsettings.types.industries

        out["industries"] = aws_sdk_taxsettings.types.industries.deserialize_json(
            data["industries"]
        )
    return out
