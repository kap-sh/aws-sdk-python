"""Generated from Smithy shape ``com.amazonaws.acmpca#DescribeCertificateAuthorityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.certificate_authority


class DescribeCertificateAuthorityResponse(TypedDict):
    certificate_authority: NotRequired[
        "aws_sdk_acm_pca.types.certificate_authority.CertificateAuthority"
    ]
    """<p>A <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_CertificateAuthority.html\">CertificateAuthority</a> structure that contains information about your private CA.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCertificateAuthorityResponse) -> dict:
    out: dict = {}
    if "certificate_authority" in value:
        import aws_sdk_acm_pca.types.certificate_authority

        out["CertificateAuthority"] = (
            aws_sdk_acm_pca.types.certificate_authority.serialize_aws_json_1_1(
                value["certificate_authority"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCertificateAuthorityResponse:
    out: DescribeCertificateAuthorityResponse = {}  # type: ignore[typeddict-item]
    if "CertificateAuthority" in data:
        import aws_sdk_acm_pca.types.certificate_authority

        out["certificate_authority"] = (
            aws_sdk_acm_pca.types.certificate_authority.deserialize_aws_json_1_1(
                data["CertificateAuthority"]
            )
        )
    return out
