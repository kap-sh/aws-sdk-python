"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetTrustStoreCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.certificate


class GetTrustStoreCertificateResponse(TypedDict):
    trust_store_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store certificate.</p>"""
    certificate: NotRequired["aws_sdk_workspaces_web.types.certificate.Certificate"]
    """<p>The certificate of the trust store certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrustStoreCertificateResponse) -> dict:
    out: dict = {}
    out["trustStoreArn"] = value["trust_store_arn"]
    if "certificate" in value:
        import aws_sdk_workspaces_web.types.certificate

        out["certificate"] = aws_sdk_workspaces_web.types.certificate.serialize_json(
            value["certificate"]
        )
    return out


def deserialize_json(data: dict) -> GetTrustStoreCertificateResponse:
    out: GetTrustStoreCertificateResponse = {}  # type: ignore[typeddict-item]
    if "trustStoreArn" in data:
        out["trust_store_arn"] = data["trustStoreArn"]
    else:
        raise DeserializationError(
            "GetTrustStoreCertificateResponse.trust_store_arn required"
        )
    if "certificate" in data:
        import aws_sdk_workspaces_web.types.certificate

        out["certificate"] = aws_sdk_workspaces_web.types.certificate.deserialize_json(
            data["certificate"]
        )
    return out
