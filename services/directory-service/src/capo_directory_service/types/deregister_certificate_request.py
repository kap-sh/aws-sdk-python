"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeregisterCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.certificate_id
    import capo_directory_service.types.directory_id


class DeregisterCertificateRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    certificate_id: "capo_directory_service.types.certificate_id.CertificateId"
    """<p>The identifier of the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterCertificateRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["CertificateId"] = value["certificate_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterCertificateRequest:
    out: DeregisterCertificateRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("DeregisterCertificateRequest.directory_id required")
    if "CertificateId" in data:
        out["certificate_id"] = data["CertificateId"]
    else:
        raise DeserializationError(
            "DeregisterCertificateRequest.certificate_id required"
        )
    return out
