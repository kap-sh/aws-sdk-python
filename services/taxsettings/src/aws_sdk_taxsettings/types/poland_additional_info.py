"""Generated from Smithy shape ``com.amazonaws.taxsettings#PolandAdditionalInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.individual_registration_number
    import aws_sdk_taxsettings.types.poland_tax_registration_number_type


class PolandAdditionalInfo(TypedDict):
    individual_registration_number: NotRequired[
        "aws_sdk_taxsettings.types.individual_registration_number.IndividualRegistrationNumber"
    ]
    """<p> The individual tax registration number (NIP). Individual NIP is valid for other taxes excluding VAT purposes. </p>"""
    is_group_vat_enabled: NotRequired["bool"]
    """<p> True if your business is a member of a VAT group with a NIP active for VAT purposes. Otherwise, this is false. </p>"""
    tax_registration_number_type: NotRequired[
        "aws_sdk_taxsettings.types.poland_tax_registration_number_type.PolandTaxRegistrationNumberType"
    ]
    """<p>The tax registration number type. Valid values are <code>EUTaxRegistrationNumber</code>, <code>LocalTaxRegistrationNumber</code>, or <code>LocalRegistrationNumber</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolandAdditionalInfo) -> dict:
    out: dict = {}
    if "individual_registration_number" in value:
        out["individualRegistrationNumber"] = value["individual_registration_number"]
    if "is_group_vat_enabled" in value:
        out["isGroupVatEnabled"] = value["is_group_vat_enabled"]
    if "tax_registration_number_type" in value:
        import aws_sdk_taxsettings.types.poland_tax_registration_number_type

        out["taxRegistrationNumberType"] = (
            aws_sdk_taxsettings.types.poland_tax_registration_number_type.serialize_json(
                value["tax_registration_number_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> PolandAdditionalInfo:
    out: PolandAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "individualRegistrationNumber" in data:
        out["individual_registration_number"] = data["individualRegistrationNumber"]
    if "isGroupVatEnabled" in data:
        out["is_group_vat_enabled"] = data["isGroupVatEnabled"]
    if "taxRegistrationNumberType" in data:
        import aws_sdk_taxsettings.types.poland_tax_registration_number_type

        out["tax_registration_number_type"] = (
            aws_sdk_taxsettings.types.poland_tax_registration_number_type.deserialize_json(
                data["taxRegistrationNumberType"]
            )
        )
    return out
