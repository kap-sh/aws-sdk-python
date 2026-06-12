"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DeleteTrustedTokenIssuerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.trusted_token_issuer_arn


class DeleteTrustedTokenIssuerRequest(TypedDict):
    trusted_token_issuer_arn: (
        "aws_sdk_sso_admin.types.trusted_token_issuer_arn.TrustedTokenIssuerArn"
    )
    """<p>Specifies the ARN of the trusted token issuer configuration to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTrustedTokenIssuerRequest) -> dict:
    out: dict = {}
    out["TrustedTokenIssuerArn"] = value["trusted_token_issuer_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTrustedTokenIssuerRequest:
    out: DeleteTrustedTokenIssuerRequest = {}  # type: ignore[typeddict-item]
    if "TrustedTokenIssuerArn" in data:
        out["trusted_token_issuer_arn"] = data["TrustedTokenIssuerArn"]
    else:
        raise DeserializationError(
            "DeleteTrustedTokenIssuerRequest.trusted_token_issuer_arn required"
        )
    return out
