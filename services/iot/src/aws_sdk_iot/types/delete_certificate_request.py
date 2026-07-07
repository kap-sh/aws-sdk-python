"""Generated from Smithy shape ``com.amazonaws.iot#DeleteCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_id
    import aws_sdk_iot.types.force_delete


class DeleteCertificateRequest(TypedDict, closed=True):
    certificate_id: "aws_sdk_iot.types.certificate_id.CertificateId"
    """<p>The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)</p>"""
    force_delete: "aws_sdk_iot.types.force_delete.ForceDelete"
    """<p>Forces the deletion of a certificate if it is inactive and is not attached to an IoT thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCertificateRequest:
    out: DeleteCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
