"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceUserTrustProviderClientConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_secret_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_trust_provider_type


class VerifiedAccessInstanceUserTrustProviderClientConfiguration(TypedDict):
    type: NotRequired[
        "aws_sdk_ec2.types.user_trust_provider_type.UserTrustProviderType"
    ]
    """<p>The trust provider type.</p>"""
    scopes: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The set of user claims to be requested from the IdP.</p>"""
    issuer: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The OIDC issuer identifier of the IdP.</p>"""
    authorization_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The authorization endpoint of the IdP.</p>"""
    public_signing_key_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public signing key endpoint.</p>"""
    token_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token endpoint of the IdP.</p>"""
    user_info_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The user info endpoint of the IdP.</p>"""
    client_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The OAuth 2.0 client identifier.</p>"""
    client_secret: NotRequired["aws_sdk_ec2.types.client_secret_type.ClientSecretType"]
    """<p>The OAuth 2.0 client secret.</p>"""
    pkce_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether Proof of Key Code Exchange (PKCE) is enabled.</p>"""
