"""Generated from Smithy shape ``com.amazonaws.taxsettings#GetTaxExemptionTypesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.tax_exemption_types

class GetTaxExemptionTypesResponse(TypedDict):
    tax_exemption_types: NotRequired["aws_sdk_taxsettings.types.tax_exemption_types.TaxExemptionTypes"]
    """<p>The supported types of tax exemptions. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetTaxExemptionTypesResponse) -> dict:
    out: dict = {}
    if "tax_exemption_types" in value:
        import aws_sdk_taxsettings.types.tax_exemption_types
        out["taxExemptionTypes"] = aws_sdk_taxsettings.types.tax_exemption_types.serialize_json(value["tax_exemption_types"])
    return out


def deserialize_json(data: dict) -> GetTaxExemptionTypesResponse:
    out: GetTaxExemptionTypesResponse = {}  # type: ignore[typeddict-item]
    if "taxExemptionTypes" in data:
        import aws_sdk_taxsettings.types.tax_exemption_types
        out["tax_exemption_types"] = aws_sdk_taxsettings.types.tax_exemption_types.deserialize_json(data["taxExemptionTypes"])
    return out