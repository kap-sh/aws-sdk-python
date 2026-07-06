"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreateTrustedTokenIssuerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.trusted_token_issuer_arn


class CreateTrustedTokenIssuerResponse(TypedDict, closed=True):
    trusted_token_issuer_arn: NotRequired[
        "aws_sdk_sso_admin.types.trusted_token_issuer_arn.TrustedTokenIssuerArn"
    ]
    """<p>The ARN of the new trusted token issuer configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrustedTokenIssuerResponse) -> dict:
    out: dict = {}
    if "trusted_token_issuer_arn" in value:
        out["TrustedTokenIssuerArn"] = value["trusted_token_issuer_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrustedTokenIssuerResponse:
    out: CreateTrustedTokenIssuerResponse = {}  # type: ignore[typeddict-item]
    if "TrustedTokenIssuerArn" in data:
        out["trusted_token_issuer_arn"] = data["TrustedTokenIssuerArn"]
    return out
