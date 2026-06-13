"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.additional_info_request
    import aws_sdk_taxsettings.types.address
    import aws_sdk_taxsettings.types.certified_email_id
    import aws_sdk_taxsettings.types.legal_name
    import aws_sdk_taxsettings.types.registration_id
    import aws_sdk_taxsettings.types.sector
    import aws_sdk_taxsettings.types.tax_registration_type
    import aws_sdk_taxsettings.types.verification_details


class TaxRegistrationEntry(TypedDict):
    registration_id: "aws_sdk_taxsettings.types.registration_id.RegistrationId"
    """<p>Your tax registration unique identifier. </p>"""
    registration_type: (
        "aws_sdk_taxsettings.types.tax_registration_type.TaxRegistrationType"
    )
    """<p> Your tax registration type. This can be either <code>VAT</code> or <code>GST</code>. </p>"""
    legal_name: NotRequired["aws_sdk_taxsettings.types.legal_name.LegalName"]
    """<p>The legal name associated with your TRN. </p> <note> <p>If you're setting a TRN in Brazil, you don't need to specify the legal name. For TRNs in other countries, you must specify the legal name.</p> </note>"""
    legal_address: NotRequired["aws_sdk_taxsettings.types.address.Address"]
    """<p>The legal address associated with your TRN.</p> <note> <p>If you're setting a TRN in Brazil for the CNPJ tax type, you don't need to specify the legal address. </p> <p>For TRNs in other countries and for CPF tax types Brazil, you must specify the legal address.</p> </note>"""
    sector: NotRequired["aws_sdk_taxsettings.types.sector.Sector"]
    """<p>The industry that describes your business. For business-to-business (B2B) customers, specify Business. For business-to-consumer (B2C) customers, specify Individual. For business-to-government (B2G), specify Government.Note that certain values may not applicable for the request country. Please refer to country specific information in API document. </p>"""
    additional_tax_information: NotRequired[
        "aws_sdk_taxsettings.types.additional_info_request.AdditionalInfoRequest"
    ]
    """<p> Additional tax information associated with your TRN. You only need to specify this parameter if Amazon Web Services collects any additional information for your country within <a>AdditionalInfoRequest</a>.</p>"""
    verification_details: NotRequired[
        "aws_sdk_taxsettings.types.verification_details.VerificationDetails"
    ]
    """<p>Additional details needed to verify your TRN information in Brazil. You only need to specify this parameter when you set a TRN in Brazil that is the CPF tax type.</p> <note> <p>Don't specify this parameter to set a TRN in Brazil of the CNPJ tax type or to set a TRN for another country. </p> </note>"""
    certified_email_id: NotRequired[
        "aws_sdk_taxsettings.types.certified_email_id.CertifiedEmailId"
    ]
    """<p>The email address to receive VAT invoices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationEntry) -> dict:
    out: dict = {}
    out["registrationId"] = value["registration_id"]
    import aws_sdk_taxsettings.types.tax_registration_type

    out["registrationType"] = (
        aws_sdk_taxsettings.types.tax_registration_type.serialize_json(
            value["registration_type"]
        )
    )
    if "legal_name" in value:
        out["legalName"] = value["legal_name"]
    if "legal_address" in value:
        import aws_sdk_taxsettings.types.address

        out["legalAddress"] = aws_sdk_taxsettings.types.address.serialize_json(
            value["legal_address"]
        )
    if "sector" in value:
        import aws_sdk_taxsettings.types.sector

        out["sector"] = aws_sdk_taxsettings.types.sector.serialize_json(value["sector"])
    if "additional_tax_information" in value:
        import aws_sdk_taxsettings.types.additional_info_request

        out["additionalTaxInformation"] = (
            aws_sdk_taxsettings.types.additional_info_request.serialize_json(
                value["additional_tax_information"]
            )
        )
    if "verification_details" in value:
        import aws_sdk_taxsettings.types.verification_details

        out["verificationDetails"] = (
            aws_sdk_taxsettings.types.verification_details.serialize_json(
                value["verification_details"]
            )
        )
    if "certified_email_id" in value:
        out["certifiedEmailId"] = value["certified_email_id"]
    return out


def deserialize_json(data: dict) -> TaxRegistrationEntry:
    out: TaxRegistrationEntry = {}  # type: ignore[typeddict-item]
    if "registrationId" in data:
        out["registration_id"] = data["registrationId"]
    else:
        raise DeserializationError("TaxRegistrationEntry.registration_id required")
    if "registrationType" in data:
        import aws_sdk_taxsettings.types.tax_registration_type

        out["registration_type"] = (
            aws_sdk_taxsettings.types.tax_registration_type.deserialize_json(
                data["registrationType"]
            )
        )
    else:
        raise DeserializationError("TaxRegistrationEntry.registration_type required")
    if "legalName" in data:
        out["legal_name"] = data["legalName"]
    if "legalAddress" in data:
        import aws_sdk_taxsettings.types.address

        out["legal_address"] = aws_sdk_taxsettings.types.address.deserialize_json(
            data["legalAddress"]
        )
    if "sector" in data:
        import aws_sdk_taxsettings.types.sector

        out["sector"] = aws_sdk_taxsettings.types.sector.deserialize_json(
            data["sector"]
        )
    if "additionalTaxInformation" in data:
        import aws_sdk_taxsettings.types.additional_info_request

        out["additional_tax_information"] = (
            aws_sdk_taxsettings.types.additional_info_request.deserialize_json(
                data["additionalTaxInformation"]
            )
        )
    if "verificationDetails" in data:
        import aws_sdk_taxsettings.types.verification_details

        out["verification_details"] = (
            aws_sdk_taxsettings.types.verification_details.deserialize_json(
                data["verificationDetails"]
            )
        )
    if "certifiedEmailId" in data:
        out["certified_email_id"] = data["certifiedEmailId"]
    return out
