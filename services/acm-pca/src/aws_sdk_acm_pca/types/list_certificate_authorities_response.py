"""Generated from Smithy shape ``com.amazonaws.acmpca#ListCertificateAuthoritiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.certificate_authorities
    import aws_sdk_acm_pca.types.next_token


class ListCertificateAuthoritiesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_acm_pca.types.next_token.NextToken"]
    """<p>When the list is truncated, this value is present and should be used for the <code>NextToken</code> parameter in a subsequent pagination request.</p>"""
    certificate_authorities: NotRequired[
        "aws_sdk_acm_pca.types.certificate_authorities.CertificateAuthorities"
    ]
    """<p>Summary information about each certificate authority you have created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificateAuthoritiesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "certificate_authorities" in value:
        import aws_sdk_acm_pca.types.certificate_authorities

        out["CertificateAuthorities"] = (
            aws_sdk_acm_pca.types.certificate_authorities.serialize_aws_json_1_1(
                value["certificate_authorities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificateAuthoritiesResponse:
    out: ListCertificateAuthoritiesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "CertificateAuthorities" in data:
        import aws_sdk_acm_pca.types.certificate_authorities

        out["certificate_authorities"] = (
            aws_sdk_acm_pca.types.certificate_authorities.deserialize_aws_json_1_1(
                data["CertificateAuthorities"]
            )
        )
    return out
