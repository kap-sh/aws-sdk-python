"""Generated from Smithy shape ``com.amazonaws.acm#GetCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_acm.types.certificate_body
    import aws_sdk_acm.types.certificate_chain


class GetCertificateResponse(TypedDict, closed=True):
    certificate: NotRequired["aws_sdk_acm.types.certificate_body.CertificateBody"]
    """<p>The ACM-issued certificate corresponding to the ARN specified as input.</p>"""
    certificate_chain: NotRequired[
        "aws_sdk_acm.types.certificate_chain.CertificateChain"
    ]
    """<p>Certificates forming the requested certificate's chain of trust. The chain consists of the certificate of the issuing CA and the intermediate certificates of any other subordinate CAs. </p>"""


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
