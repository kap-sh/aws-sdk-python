"""Generated from Smithy shape ``com.amazonaws.iot#DeleteCACertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_id


class DeleteCACertificateRequest(TypedDict):
    certificate_id: "aws_sdk_iot.types.certificate_id.CertificateId"
    """<p>The ID of the certificate to delete. (The last part of the certificate ARN contains the certificate ID.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCACertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCACertificateRequest:
    out: DeleteCACertificateRequest = {}  # type: ignore[typeddict-item]
    return out
