"""Generated from Smithy shape ``com.amazonaws.taxsettings#VerificationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.date_of_birth
    import aws_sdk_taxsettings.types.tax_registration_documents


class VerificationDetails(TypedDict):
    date_of_birth: NotRequired["aws_sdk_taxsettings.types.date_of_birth.DateOfBirth"]
    """<p>Date of birth to verify your submitted TRN. Use the <code>YYYY-MM-DD</code> format.</p>"""
    tax_registration_documents: NotRequired[
        "aws_sdk_taxsettings.types.tax_registration_documents.TaxRegistrationDocuments"
    ]
    """<p>The tax registration document, which is required for specific countries such as Bangladesh, Kenya, South Korea and Spain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerificationDetails) -> dict:
    out: dict = {}
    if "date_of_birth" in value:
        out["dateOfBirth"] = value["date_of_birth"]
    if "tax_registration_documents" in value:
        import aws_sdk_taxsettings.types.tax_registration_documents

        out["taxRegistrationDocuments"] = (
            aws_sdk_taxsettings.types.tax_registration_documents.serialize_json(
                value["tax_registration_documents"]
            )
        )
    return out


def deserialize_json(data: dict) -> VerificationDetails:
    out: VerificationDetails = {}  # type: ignore[typeddict-item]
    if "dateOfBirth" in data:
        out["date_of_birth"] = data["dateOfBirth"]
    if "taxRegistrationDocuments" in data:
        import aws_sdk_taxsettings.types.tax_registration_documents

        out["tax_registration_documents"] = (
            aws_sdk_taxsettings.types.tax_registration_documents.deserialize_json(
                data["taxRegistrationDocuments"]
            )
        )
    return out
