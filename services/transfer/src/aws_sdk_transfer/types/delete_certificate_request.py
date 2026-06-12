"""Generated from Smithy shape ``com.amazonaws.transfer#DeleteCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.certificate_id


class DeleteCertificateRequest(TypedDict):
    certificate_id: "aws_sdk_transfer.types.certificate_id.CertificateId"
    """<p>The identifier of the certificate object that you are deleting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateId"] = value["certificate_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCertificateRequest:
    out: DeleteCertificateRequest = {}  # type: ignore[typeddict-item]
    if "CertificateId" in data:
        out["certificate_id"] = data["CertificateId"]
    else:
        raise DeserializationError("DeleteCertificateRequest.certificate_id required")
    return out
