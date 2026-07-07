"""Generated from Smithy shape ``com.amazonaws.workspaces#CertificateBasedAuthProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.certificate_authority_arn
    import aws_sdk_workspaces.types.certificate_based_auth_status_enum


class CertificateBasedAuthProperties(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_workspaces.types.certificate_based_auth_status_enum.CertificateBasedAuthStatusEnum"
    ]
    """<p>The status of the certificate-based authentication properties.</p>"""
    certificate_authority_arn: NotRequired[
        "aws_sdk_workspaces.types.certificate_authority_arn.CertificateAuthorityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Certificate Manager Private CA resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateBasedAuthProperties) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_workspaces.types.certificate_based_auth_status_enum

        out["Status"] = (
            aws_sdk_workspaces.types.certificate_based_auth_status_enum.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateBasedAuthProperties:
    out: CertificateBasedAuthProperties = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_workspaces.types.certificate_based_auth_status_enum

        out["status"] = (
            aws_sdk_workspaces.types.certificate_based_auth_status_enum.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    return out
