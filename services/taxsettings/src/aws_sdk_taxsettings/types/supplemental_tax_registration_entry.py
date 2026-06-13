"""Generated from Smithy shape ``com.amazonaws.taxsettings#SupplementalTaxRegistrationEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.address
    import aws_sdk_taxsettings.types.legal_name
    import aws_sdk_taxsettings.types.registration_id
    import aws_sdk_taxsettings.types.supplemental_tax_registration_type


class SupplementalTaxRegistrationEntry(TypedDict):
    registration_id: "aws_sdk_taxsettings.types.registration_id.RegistrationId"
    """<p> The supplemental TRN unique identifier. </p>"""
    registration_type: "aws_sdk_taxsettings.types.supplemental_tax_registration_type.SupplementalTaxRegistrationType"
    """<p> Type of supplemental TRN. Currently, this can only be VAT. </p>"""
    legal_name: "aws_sdk_taxsettings.types.legal_name.LegalName"
    """<p> The legal name associated with your TRN registration. </p>"""
    address: "aws_sdk_taxsettings.types.address.Address"


# --- restJson1 ser/de ---
def serialize_json(value: SupplementalTaxRegistrationEntry) -> dict:
    out: dict = {}
    out["registrationId"] = value["registration_id"]
    import aws_sdk_taxsettings.types.supplemental_tax_registration_type

    out["registrationType"] = (
        aws_sdk_taxsettings.types.supplemental_tax_registration_type.serialize_json(
            value["registration_type"]
        )
    )
    out["legalName"] = value["legal_name"]
    import aws_sdk_taxsettings.types.address

    out["address"] = aws_sdk_taxsettings.types.address.serialize_json(value["address"])
    return out


def deserialize_json(data: dict) -> SupplementalTaxRegistrationEntry:
    out: SupplementalTaxRegistrationEntry = {}  # type: ignore[typeddict-item]
    if "registrationId" in data:
        out["registration_id"] = data["registrationId"]
    else:
        raise DeserializationError(
            "SupplementalTaxRegistrationEntry.registration_id required"
        )
    if "registrationType" in data:
        import aws_sdk_taxsettings.types.supplemental_tax_registration_type

        out["registration_type"] = (
            aws_sdk_taxsettings.types.supplemental_tax_registration_type.deserialize_json(
                data["registrationType"]
            )
        )
    else:
        raise DeserializationError(
            "SupplementalTaxRegistrationEntry.registration_type required"
        )
    if "legalName" in data:
        out["legal_name"] = data["legalName"]
    else:
        raise DeserializationError(
            "SupplementalTaxRegistrationEntry.legal_name required"
        )
    if "address" in data:
        import aws_sdk_taxsettings.types.address

        out["address"] = aws_sdk_taxsettings.types.address.deserialize_json(
            data["address"]
        )
    else:
        raise DeserializationError("SupplementalTaxRegistrationEntry.address required")
    return out
