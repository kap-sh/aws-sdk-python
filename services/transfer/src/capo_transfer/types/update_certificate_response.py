"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.certificate_id


class UpdateCertificateResponse(TypedDict, closed=True):
    certificate_id: "capo_transfer.types.certificate_id.CertificateId"
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
