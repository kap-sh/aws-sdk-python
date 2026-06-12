"""Generated from Smithy shape ``com.amazonaws.acmpca#GetCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.certificate_body
    import aws_sdk_acm_pca.types.certificate_chain


class GetCertificateResponse(TypedDict):
    certificate: NotRequired["aws_sdk_acm_pca.types.certificate_body.CertificateBody"]
    """<p>The base64 PEM-encoded certificate specified by the <code>CertificateArn</code> parameter.</p>"""
    certificate_chain: NotRequired[
        "aws_sdk_acm_pca.types.certificate_chain.CertificateChain"
    ]
    """<p>The base64 PEM-encoded certificate chain that chains up to the root CA certificate that you used to sign your private CA certificate. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "certificate_chain" in value:
        out["CertificateChain"] = value["certificate_chain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCertificateResponse:
    out: GetCertificateResponse = {}  # type: ignore[typeddict-item]
    if "Certificate" in data:
        out["certificate"] = data["Certificate"]
    if "CertificateChain" in data:
        out["certificate_chain"] = data["CertificateChain"]
    return out
