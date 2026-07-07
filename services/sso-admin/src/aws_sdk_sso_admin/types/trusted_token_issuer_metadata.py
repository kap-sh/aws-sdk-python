"""Generated from Smithy shape ``com.amazonaws.ssoadmin#TrustedTokenIssuerMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.trusted_token_issuer_arn
    import aws_sdk_sso_admin.types.trusted_token_issuer_name
    import aws_sdk_sso_admin.types.trusted_token_issuer_type


class TrustedTokenIssuerMetadata(TypedDict, closed=True):
    trusted_token_issuer_arn: NotRequired[
        "aws_sdk_sso_admin.types.trusted_token_issuer_arn.TrustedTokenIssuerArn"
    ]
    """<p>The ARN of the trusted token issuer configuration in the instance of IAM Identity Center.</p>"""
    name: NotRequired[
        "aws_sdk_sso_admin.types.trusted_token_issuer_name.TrustedTokenIssuerName"
    ]
    """<p>The name of the trusted token issuer configuration in the instance of IAM Identity Center.</p>"""
    trusted_token_issuer_type: NotRequired[
        "aws_sdk_sso_admin.types.trusted_token_issuer_type.TrustedTokenIssuerType"
    ]
    """<p>The type of trusted token issuer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedTokenIssuerMetadata) -> dict:
    out: dict = {}
    if "trusted_token_issuer_arn" in value:
        out["TrustedTokenIssuerArn"] = value["trusted_token_issuer_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "trusted_token_issuer_type" in value:
        import aws_sdk_sso_admin.types.trusted_token_issuer_type

        out["TrustedTokenIssuerType"] = (
            aws_sdk_sso_admin.types.trusted_token_issuer_type.serialize_aws_json_1_1(
                value["trusted_token_issuer_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedTokenIssuerMetadata:
    out: TrustedTokenIssuerMetadata = {}  # type: ignore[typeddict-item]
    if "TrustedTokenIssuerArn" in data:
        out["trusted_token_issuer_arn"] = data["TrustedTokenIssuerArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "TrustedTokenIssuerType" in data:
        import aws_sdk_sso_admin.types.trusted_token_issuer_type

        out["trusted_token_issuer_type"] = (
            aws_sdk_sso_admin.types.trusted_token_issuer_type.deserialize_aws_json_1_1(
                data["TrustedTokenIssuerType"]
            )
        )
    return out
