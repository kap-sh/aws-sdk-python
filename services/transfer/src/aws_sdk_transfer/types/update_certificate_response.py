"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.certificate_id


class UpdateCertificateResponse(TypedDict):
    certificate_id: "aws_sdk_transfer.types.certificate_id.CertificateId"
    """<p>Returns the identifier of the certificate object that you are updating.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCertificateResponse) -> dict:
    out: dict = {}
    out["CertificateId"] = value["certificate_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCertificateResponse:
    out: UpdateCertificateResponse = {}  # type: ignore[typeddict-item]
    if "CertificateId" in data:
        out["certificate_id"] = data["CertificateId"]
    else:
        raise DeserializationError("UpdateCertificateResponse.certificate_id required")
    return out
