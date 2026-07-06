"""Generated from Smithy shape ``com.amazonaws.ecr#AuthorizationData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.base64
    import aws_sdk_ecr.types.expiration_timestamp
    import aws_sdk_ecr.types.proxy_endpoint


class AuthorizationData(TypedDict, closed=True):
    authorization_token: NotRequired["aws_sdk_ecr.types.base64.Base64"]
    """<p>A base64-encoded string that contains authorization data for the specified Amazon ECR registry. When the string is decoded, it is presented in the format <code>user:password</code> for private registry authentication using <code>docker login</code>.</p>"""
    expires_at: NotRequired[
        "aws_sdk_ecr.types.expiration_timestamp.ExpirationTimestamp"
    ]
    """<p>The Unix time in seconds and milliseconds when the authorization token expires. Authorization tokens are valid for 12 hours.</p>"""
    proxy_endpoint: NotRequired["aws_sdk_ecr.types.proxy_endpoint.ProxyEndpoint"]
    """<p>The registry URL to use for this authorization token in a <code>docker login</code> command. The Amazon ECR registry URL format is <code>https://aws_account_id.dkr.ecr.region.amazonaws.com</code>. For example, <code>https://012345678910.dkr.ecr.us-east-1.amazonaws.com</code>.. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthorizationData) -> dict:
    out: dict = {}
    if "authorization_token" in value:
        out["authorizationToken"] = value["authorization_token"]
    if "expires_at" in value:
        import aws_sdk_ecr.types.expiration_timestamp

        out["expiresAt"] = (
            aws_sdk_ecr.types.expiration_timestamp.serialize_aws_json_1_1(
                value["expires_at"]
            )
        )
    if "proxy_endpoint" in value:
        out["proxyEndpoint"] = value["proxy_endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthorizationData:
    out: AuthorizationData = {}  # type: ignore[typeddict-item]
    if "authorizationToken" in data:
        out["authorization_token"] = data["authorizationToken"]
    if "expiresAt" in data:
        import aws_sdk_ecr.types.expiration_timestamp

        out["expires_at"] = (
            aws_sdk_ecr.types.expiration_timestamp.deserialize_aws_json_1_1(
                data["expiresAt"]
            )
        )
    if "proxyEndpoint" in data:
        out["proxy_endpoint"] = data["proxyEndpoint"]
    return out
