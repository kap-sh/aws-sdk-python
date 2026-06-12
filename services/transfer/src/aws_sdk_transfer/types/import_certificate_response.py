"""Generated from Smithy shape ``com.amazonaws.transfer#ImportCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.certificate_id


class ImportCertificateResponse(TypedDict):
    certificate_id: "aws_sdk_transfer.types.certificate_id.CertificateId"
    """<p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCertificateResponse) -> dict:
    out: dict = {}
    out["CertificateId"] = value["certificate_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportCertificateResponse:
    out: ImportCertificateResponse = {}  # type: ignore[typeddict-item]
    if "CertificateId" in data:
        out["certificate_id"] = data["CertificateId"]
    else:
        raise DeserializationError("ImportCertificateResponse.certificate_id required")
    return out
