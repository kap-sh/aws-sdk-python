"""Generated from Smithy shape ``com.amazonaws.acmpca#GetCertificateAuthorityCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.certificate_body
    import aws_sdk_acm_pca.types.certificate_chain


class GetCertificateAuthorityCertificateResponse(TypedDict):
    certificate: NotRequired["aws_sdk_acm_pca.types.certificate_body.CertificateBody"]
    """<p>Base64-encoded certificate authority (CA) certificate.</p>"""
    certificate_chain: NotRequired[
        "aws_sdk_acm_pca.types.certificate_chain.CertificateChain"
    ]
    """<p>Base64-encoded certificate chain that includes any intermediate certificates and chains up to root certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. If this is a root CA, the value will be null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCertificateAuthorityCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "certificate_chain" in value:
        out["CertificateChain"] = value["certificate_chain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCertificateAuthorityCertificateResponse:
    out: GetCertificateAuthorityCertificateResponse = {}  # type: ignore[typeddict-item]
    if "Certificate" in data:
        out["certificate"] = data["Certificate"]
    if "CertificateChain" in data:
        out["certificate_chain"] = data["CertificateChain"]
    return out
