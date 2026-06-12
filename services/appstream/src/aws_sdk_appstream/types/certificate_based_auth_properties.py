"""Generated from Smithy shape ``com.amazonaws.appstream#CertificateBasedAuthProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.certificate_based_auth_status


class CertificateBasedAuthProperties(TypedDict):
    status: NotRequired[
        "aws_sdk_appstream.types.certificate_based_auth_status.CertificateBasedAuthStatus"
    ]
    """<p>The status of the certificate-based authentication properties.</p>"""
    certificate_authority_arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The ARN of the AWS Certificate Manager Private CA resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateBasedAuthProperties) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_appstream.types.certificate_based_auth_status

        out["Status"] = (
            aws_sdk_appstream.types.certificate_based_auth_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateBasedAuthProperties:
    out: CertificateBasedAuthProperties = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_appstream.types.certificate_based_auth_status

        out["status"] = (
            aws_sdk_appstream.types.certificate_based_auth_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    return out
