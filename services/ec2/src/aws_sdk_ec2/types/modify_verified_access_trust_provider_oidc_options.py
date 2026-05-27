"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessTrustProviderOidcOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_secret_type
    import aws_sdk_ec2.types.string


class ModifyVerifiedAccessTrustProviderOidcOptions(TypedDict):
    issuer: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The OIDC issuer.</p>"""
    authorization_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The OIDC authorization endpoint.</p>"""
    token_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The OIDC token endpoint.</p>"""
    user_info_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The OIDC user info endpoint.</p>"""
    client_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The client identifier.</p>"""
    client_secret: NotRequired["aws_sdk_ec2.types.client_secret_type.ClientSecretType"]
    """<p>The client secret.</p>"""
    scope: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>OpenID Connect (OIDC) scopes are used by an application during authentication to authorize access to a user's details. Each scope returns a specific set of user attributes.</p>"""
