"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationWithJurisdiction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.additional_info_response
    import aws_sdk_taxsettings.types.certified_email_id
    import aws_sdk_taxsettings.types.jurisdiction
    import aws_sdk_taxsettings.types.legal_name
    import aws_sdk_taxsettings.types.registration_id
    import aws_sdk_taxsettings.types.sector
    import aws_sdk_taxsettings.types.tax_document_metadatas
    import aws_sdk_taxsettings.types.tax_registration_status
    import aws_sdk_taxsettings.types.tax_registration_type


class TaxRegistrationWithJurisdiction(TypedDict):
    registration_id: "aws_sdk_taxsettings.types.registration_id.RegistrationId"
    """<p>Your tax registration unique identifier. </p>"""
    registration_type: (
        "aws_sdk_taxsettings.types.tax_registration_type.TaxRegistrationType"
    )
    """<p> The type of your tax registration. This can be either <code>VAT</code> or <code>GST</code>. </p>"""
    legal_name: "aws_sdk_taxsettings.types.legal_name.LegalName"
    """<p>The legal name associated with your TRN information. </p>"""
    status: "aws_sdk_taxsettings.types.tax_registration_status.TaxRegistrationStatus"
    """<p>The status of your TRN. This can be either <code>Verified</code>, <code>Pending</code>, <code>Deleted</code>, or <code>Rejected</code>. </p>"""
    sector: NotRequired["aws_sdk_taxsettings.types.sector.Sector"]
    """<p>The industry that describes your business. For business-to-business (B2B) customers, specify Business. For business-to-consumer (B2C) customers, specify Individual. For business-to-government (B2G), specify Government.Note that certain values may not applicable for the request country. Please refer to country specific information in API document. </p>"""
    tax_document_metadatas: NotRequired[
        "aws_sdk_taxsettings.types.tax_document_metadatas.TaxDocumentMetadatas"
    ]
    """<p>The metadata for your tax document.</p>"""
    certified_email_id: NotRequired[
        "aws_sdk_taxsettings.types.certified_email_id.CertifiedEmailId"
    ]
    """<p>The email address to receive VAT invoices.</p>"""
    additional_tax_information: NotRequired[
        "aws_sdk_taxsettings.types.additional_info_response.AdditionalInfoResponse"
    ]
    """<p>Additional tax information associated with your TRN. </p>"""
    jurisdiction: "aws_sdk_taxsettings.types.jurisdiction.Jurisdiction"
    """<p> The jurisdiction associated with your TRN information. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationWithJurisdiction) -> dict:
    out: dict = {}
    out["registrationId"] = value["registration_id"]
    import aws_sdk_taxsettings.types.tax_registration_type

    out["registrationType"] = (
        aws_sdk_taxsettings.types.tax_registration_type.serialize_json(
            value["registration_type"]
        )
    )
    out["legalName"] = value["legal_name"]
    import aws_sdk_taxsettings.types.tax_registration_status

    out["status"] = aws_sdk_taxsettings.types.tax_registration_status.serialize_json(
        value["status"]
    )
    if "sector" in value:
        import aws_sdk_taxsettings.types.sector

        out["sector"] = aws_sdk_taxsettings.types.sector.serialize_json(value["sector"])
    if "tax_document_metadatas" in value:
        import aws_sdk_taxsettings.types.tax_document_metadatas

        out["taxDocumentMetadatas"] = (
            aws_sdk_taxsettings.types.tax_document_metadatas.serialize_json(
                value["tax_document_metadatas"]
            )
        )
    if "certified_email_id" in value:
        out["certifiedEmailId"] = value["certified_email_id"]
    if "additional_tax_information" in value:
        import aws_sdk_taxsettings.types.additional_info_response

        out["additionalTaxInformation"] = (
            aws_sdk_taxsettings.types.additional_info_response.serialize_json(
                value["additional_tax_information"]
            )
        )
    import aws_sdk_taxsettings.types.jurisdiction

    out["jurisdiction"] = aws_sdk_taxsettings.types.jurisdiction.serialize_json(
        value["jurisdiction"]
    )
    return out


def deserialize_json(data: dict) -> TaxRegistrationWithJurisdiction:
    out: TaxRegistrationWithJurisdiction = {}  # type: ignore[typeddict-item]
    if "registrationId" in data:
        out["registration_id"] = data["registrationId"]
    else:
        raise DeserializationError(
            "TaxRegistrationWithJurisdiction.registration_id required"
        )
    if "registrationType" in data:
        import aws_sdk_taxsettings.types.tax_registration_type

        out["registration_type"] = (
            aws_sdk_taxsettings.types.tax_registration_type.deserialize_json(
                data["registrationType"]
            )
        )
    else:
        raise DeserializationError(
            "TaxRegistrationWithJurisdiction.registration_type required"
        )
    if "legalName" in data:
        out["legal_name"] = data["legalName"]
    else:
        raise DeserializationError(
            "TaxRegistrationWithJurisdiction.legal_name required"
        )
    if "status" in data:
        import aws_sdk_taxsettings.types.tax_registration_status

        out["status"] = (
            aws_sdk_taxsettings.types.tax_registration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("TaxRegistrationWithJurisdiction.status required")
    if "sector" in data:
        import aws_sdk_taxsettings.types.sector

        out["sector"] = aws_sdk_taxsettings.types.sector.deserialize_json(
            data["sector"]
        )
    if "taxDocumentMetadatas" in data:
        import aws_sdk_taxsettings.types.tax_document_metadatas

        out["tax_document_metadatas"] = (
            aws_sdk_taxsettings.types.tax_document_metadatas.deserialize_json(
                data["taxDocumentMetadatas"]
            )
        )
    if "certifiedEmailId" in data:
        out["certified_email_id"] = data["certifiedEmailId"]
    if "additionalTaxInformation" in data:
        import aws_sdk_taxsettings.types.additional_info_response

        out["additional_tax_information"] = (
            aws_sdk_taxsettings.types.additional_info_response.deserialize_json(
                data["additionalTaxInformation"]
            )
        )
    if "jurisdiction" in data:
        import aws_sdk_taxsettings.types.jurisdiction

        out["jurisdiction"] = aws_sdk_taxsettings.types.jurisdiction.deserialize_json(
            data["jurisdiction"]
        )
    else:
        raise DeserializationError(
            "TaxRegistrationWithJurisdiction.jurisdiction required"
        )
    return out
