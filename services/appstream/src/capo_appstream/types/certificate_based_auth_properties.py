"""Generated from Smithy shape ``com.amazonaws.appstream#CertificateBasedAuthProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.certificate_based_auth_status


class CertificateBasedAuthProperties(TypedDict, closed=True):
    status: NotRequired[
        "capo_appstream.types.certificate_based_auth_status.CertificateBasedAuthStatus"
    ]
    """<p>The status of the certificate-based authentication properties.</p>"""
    certificate_authority_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the AWS Certificate Manager Private CA resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateBasedAuthProperties) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_appstream.types.certificate_based_auth_status

        out["Status"] = (
            capo_appstream.types.certificate_based_auth_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateBasedAuthProperties:
    out: CertificateBasedAuthProperties = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_appstream.types.certificate_based_auth_status

        out["status"] = (
            capo_appstream.types.certificate_based_auth_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    return out
