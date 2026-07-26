"""Generated from Smithy shape ``com.amazonaws.taxsettings#GetTaxRegistrationDocumentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.destination_file_path
    import capo_taxsettings.types.url


class GetTaxRegistrationDocumentResponse(TypedDict, closed=True):
    destination_file_path: NotRequired[
        "capo_taxsettings.types.destination_file_path.DestinationFilePath"
    ]
    """<p>The file path of the Amazon S3 bucket where you want to download your tax document to.</p>"""
    presigned_s3_url: NotRequired["capo_taxsettings.types.url.Url"]
    """<p>The Amazon S3 presigned URL of the tax registration document. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTaxRegistrationDocumentResponse) -> dict:
    out: dict = {}
    if "destination_file_path" in value:
        out["destinationFilePath"] = value["destination_file_path"]
    if "presigned_s3_url" in value:
        out["presignedS3Url"] = value["presigned_s3_url"]
    return out


def deserialize_json(data: dict) -> GetTaxRegistrationDocumentResponse:
    out: GetTaxRegistrationDocumentResponse = {}  # type: ignore[typeddict-item]
    if "destinationFilePath" in data:
        out["destination_file_path"] = data["destinationFilePath"]
    if "presignedS3Url" in data:
        out["presigned_s3_url"] = data["presignedS3Url"]
    return out
