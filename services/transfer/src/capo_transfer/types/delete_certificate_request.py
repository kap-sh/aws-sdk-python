"""Generated from Smithy shape ``com.amazonaws.transfer#DeleteCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.certificate_id


class DeleteCertificateRequest(TypedDict, closed=True):
    certificate_id: "capo_transfer.types.certificate_id.CertificateId"
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
