"""Generated from Smithy shape ``com.amazonaws.taxsettings#SaudiArabiaAdditionalInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.saudi_arabia_tax_registration_number_type

class SaudiArabiaAdditionalInfo(TypedDict):
    tax_registration_number_type: NotRequired["aws_sdk_taxsettings.types.saudi_arabia_tax_registration_number_type.SaudiArabiaTaxRegistrationNumberType"]
    """<p> The tax registration number type. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: SaudiArabiaAdditionalInfo) -> dict:
    out: dict = {}
    if "tax_registration_number_type" in value:
        import aws_sdk_taxsettings.types.saudi_arabia_tax_registration_number_type
        out["taxRegistrationNumberType"] = aws_sdk_taxsettings.types.saudi_arabia_tax_registration_number_type.serialize_json(value["tax_registration_number_type"])
    return out


def deserialize_json(data: dict) -> SaudiArabiaAdditionalInfo:
    out: SaudiArabiaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "taxRegistrationNumberType" in data:
        import aws_sdk_taxsettings.types.saudi_arabia_tax_registration_number_type
        out["tax_registration_number_type"] = aws_sdk_taxsettings.types.saudi_arabia_tax_registration_number_type.deserialize_json(data["taxRegistrationNumberType"])
    return out