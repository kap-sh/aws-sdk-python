"""Generated from Smithy shape ``com.amazonaws.taxsettings#UzbekistanAdditionalInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.uzbekistan_tax_registration_number_type
    import aws_sdk_taxsettings.types.vat_registration_number


class UzbekistanAdditionalInfo(TypedDict):
    tax_registration_number_type: NotRequired[
        "aws_sdk_taxsettings.types.uzbekistan_tax_registration_number_type.UzbekistanTaxRegistrationNumberType"
    ]
    """<p> The tax registration number type. The tax registration number type valid values are <code>Business</code> and <code>Individual</code>. </p>"""
    vat_registration_number: NotRequired[
        "aws_sdk_taxsettings.types.vat_registration_number.VatRegistrationNumber"
    ]
    """<p> The unique 12-digit number issued to identify VAT-registered identities in Uzbekistan. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UzbekistanAdditionalInfo) -> dict:
    out: dict = {}
    if "tax_registration_number_type" in value:
        import aws_sdk_taxsettings.types.uzbekistan_tax_registration_number_type

        out["taxRegistrationNumberType"] = (
            aws_sdk_taxsettings.types.uzbekistan_tax_registration_number_type.serialize_json(
                value["tax_registration_number_type"]
            )
        )
    if "vat_registration_number" in value:
        out["vatRegistrationNumber"] = value["vat_registration_number"]
    return out


def deserialize_json(data: dict) -> UzbekistanAdditionalInfo:
    out: UzbekistanAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "taxRegistrationNumberType" in data:
        import aws_sdk_taxsettings.types.uzbekistan_tax_registration_number_type

        out["tax_registration_number_type"] = (
            aws_sdk_taxsettings.types.uzbekistan_tax_registration_number_type.deserialize_json(
                data["taxRegistrationNumberType"]
            )
        )
    if "vatRegistrationNumber" in data:
        out["vat_registration_number"] = data["vatRegistrationNumber"]
    return out
