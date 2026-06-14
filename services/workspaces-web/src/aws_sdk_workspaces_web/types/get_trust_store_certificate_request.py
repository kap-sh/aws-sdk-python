"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetTrustStoreCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.certificate_thumbprint


class GetTrustStoreCertificateRequest(TypedDict):
    trust_store_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store certificate.</p>"""
    thumbprint: (
        "aws_sdk_workspaces_web.types.certificate_thumbprint.CertificateThumbprint"
    )
    """<p>The thumbprint of the trust store certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrustStoreCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTrustStoreCertificateRequest:
    out: GetTrustStoreCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
