"""Generated from Smithy shape ``com.amazonaws.ec2#FederatedAuthenticationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class FederatedAuthenticationRequest(TypedDict):
    saml_provider_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM SAML identity provider.</p>"""
    self_service_saml_provider_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM SAML identity provider for the self-service portal.</p>"""
