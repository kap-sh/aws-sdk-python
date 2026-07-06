"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxExemptionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.generic_string
    import aws_sdk_taxsettings.types.tax_exemptions


class TaxExemptionDetails(TypedDict, closed=True):
    tax_exemptions: NotRequired[
        "aws_sdk_taxsettings.types.tax_exemptions.TaxExemptions"
    ]
    """<p>Tax exemptions. </p>"""
    heritage_obtained_details: NotRequired["bool"]
    """<p>The indicator if the tax exemption is inherited from the consolidated billing family management account. </p>"""
    heritage_obtained_parent_entity: NotRequired[
        "aws_sdk_taxsettings.types.generic_string.GenericString"
    ]
    """<p>The consolidated billing family management account the tax exemption inherited from. </p>"""
    heritage_obtained_reason: NotRequired[
        "aws_sdk_taxsettings.types.generic_string.GenericString"
    ]
    """<p>The reason of the heritage inheritance. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxExemptionDetails) -> dict:
    out: dict = {}
    if "tax_exemptions" in value:
        import aws_sdk_taxsettings.types.tax_exemptions

        out["taxExemptions"] = aws_sdk_taxsettings.types.tax_exemptions.serialize_json(
            value["tax_exemptions"]
        )
    if "heritage_obtained_details" in value:
        out["heritageObtainedDetails"] = value["heritage_obtained_details"]
    if "heritage_obtained_parent_entity" in value:
        out["heritageObtainedParentEntity"] = value["heritage_obtained_parent_entity"]
    if "heritage_obtained_reason" in value:
        out["heritageObtainedReason"] = value["heritage_obtained_reason"]
    return out


def deserialize_json(data: dict) -> TaxExemptionDetails:
    out: TaxExemptionDetails = {}  # type: ignore[typeddict-item]
    if "taxExemptions" in data:
        import aws_sdk_taxsettings.types.tax_exemptions

        out["tax_exemptions"] = (
            aws_sdk_taxsettings.types.tax_exemptions.deserialize_json(
                data["taxExemptions"]
            )
        )
    if "heritageObtainedDetails" in data:
        out["heritage_obtained_details"] = data["heritageObtainedDetails"]
    if "heritageObtainedParentEntity" in data:
        out["heritage_obtained_parent_entity"] = data["heritageObtainedParentEntity"]
    if "heritageObtainedReason" in data:
        out["heritage_obtained_reason"] = data["heritageObtainedReason"]
    return out
