"""Generated from Smithy shape ``com.amazonaws.ec2#OidcOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_secret_type
    import aws_sdk_ec2.types.string


class OidcOptions(TypedDict):
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
    """<p>The OpenID Connect (OIDC) scope specified.</p>"""
