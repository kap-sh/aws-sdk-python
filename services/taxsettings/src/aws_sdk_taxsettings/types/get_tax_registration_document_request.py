"""Generated from Smithy shape ``com.amazonaws.taxsettings#GetTaxRegistrationDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.destination_s3_location
    import aws_sdk_taxsettings.types.tax_document_metadata


class GetTaxRegistrationDocumentRequest(TypedDict, closed=True):
    destination_s3_location: NotRequired[
        "aws_sdk_taxsettings.types.destination_s3_location.DestinationS3Location"
    ]
    """<p>The Amazon S3 bucket that you specify to download your tax documents to.</p>"""
    tax_document_metadata: (
        "aws_sdk_taxsettings.types.tax_document_metadata.TaxDocumentMetadata"
    )
    """<p>The metadata for your tax document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTaxRegistrationDocumentRequest) -> dict:
    out: dict = {}
    if "destination_s3_location" in value:
        import aws_sdk_taxsettings.types.destination_s3_location

        out["destinationS3Location"] = (
            aws_sdk_taxsettings.types.destination_s3_location.serialize_json(
                value["destination_s3_location"]
            )
        )
    import aws_sdk_taxsettings.types.tax_document_metadata

    out["taxDocumentMetadata"] = (
        aws_sdk_taxsettings.types.tax_document_metadata.serialize_json(
            value["tax_document_metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTaxRegistrationDocumentRequest:
    out: GetTaxRegistrationDocumentRequest = {}  # type: ignore[typeddict-item]
    if "destinationS3Location" in data:
        import aws_sdk_taxsettings.types.destination_s3_location

        out["destination_s3_location"] = (
            aws_sdk_taxsettings.types.destination_s3_location.deserialize_json(
                data["destinationS3Location"]
            )
        )
    if "taxDocumentMetadata" in data:
        import aws_sdk_taxsettings.types.tax_document_metadata

        out["tax_document_metadata"] = (
            aws_sdk_taxsettings.types.tax_document_metadata.deserialize_json(
                data["taxDocumentMetadata"]
            )
        )
    else:
        raise DeserializationError(
            "GetTaxRegistrationDocumentRequest.tax_document_metadata required"
        )
    return out
