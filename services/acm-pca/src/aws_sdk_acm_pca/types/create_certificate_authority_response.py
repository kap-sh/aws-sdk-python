"""Generated from Smithy shape ``com.amazonaws.acmpca#CreateCertificateAuthorityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.arn


class CreateCertificateAuthorityResponse(TypedDict):
    certificate_authority_arn: NotRequired["aws_sdk_acm_pca.types.arn.Arn"]
    """<p>If successful, the Amazon Resource Name (ARN) of the certificate authority (CA). This is of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCertificateAuthorityResponse) -> dict:
    out: dict = {}
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCertificateAuthorityResponse:
    out: CreateCertificateAuthorityResponse = {}  # type: ignore[typeddict-item]
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    return out
