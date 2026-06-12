"""Generated from Smithy shape ``com.amazonaws.ecrpublic#AuthorizationData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.base64
    import aws_sdk_ecr_public.types.expiration_timestamp


class AuthorizationData(TypedDict):
    authorization_token: NotRequired["aws_sdk_ecr_public.types.base64.Base64"]
    """<p>A base64-encoded string that contains authorization data for a public Amazon ECR registry. When the string is decoded, it's presented in the format <code>user:password</code> for public registry authentication using <code>docker login</code>.</p>"""
    expires_at: NotRequired[
        "aws_sdk_ecr_public.types.expiration_timestamp.ExpirationTimestamp"
    ]
    """<p>The Unix time in seconds and milliseconds when the authorization token expires. Authorization tokens are valid for 12 hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthorizationData) -> dict:
    out: dict = {}
    if "authorization_token" in value:
        out["authorizationToken"] = value["authorization_token"]
    if "expires_at" in value:
        import aws_sdk_ecr_public.types.expiration_timestamp

        out["expiresAt"] = (
            aws_sdk_ecr_public.types.expiration_timestamp.serialize_aws_json_1_1(
                value["expires_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthorizationData:
    out: AuthorizationData = {}  # type: ignore[typeddict-item]
    if "authorizationToken" in data:
        out["authorization_token"] = data["authorizationToken"]
    if "expiresAt" in data:
        import aws_sdk_ecr_public.types.expiration_timestamp

        out["expires_at"] = (
            aws_sdk_ecr_public.types.expiration_timestamp.deserialize_aws_json_1_1(
                data["expiresAt"]
            )
        )
    return out
