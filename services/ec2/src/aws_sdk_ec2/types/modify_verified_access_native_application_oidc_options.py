"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessNativeApplicationOidcOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_secret_type
    import aws_sdk_ec2.types.string


class ModifyVerifiedAccessNativeApplicationOidcOptions(TypedDict):
    public_signing_key_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public signing key endpoint.</p>"""
    issuer: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The OIDC issuer identifier of the IdP.</p>"""
    authorization_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The authorization endpoint of the IdP.</p>"""
    token_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token endpoint of the IdP.</p>"""
    user_info_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The user info endpoint of the IdP.</p>"""
    client_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The OAuth 2.0 client identifier.</p>"""
    client_secret: NotRequired["aws_sdk_ec2.types.client_secret_type.ClientSecretType"]
    """<p>The OAuth 2.0 client secret.</p>"""
    scope: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The set of user claims to be requested from the IdP.</p>"""
