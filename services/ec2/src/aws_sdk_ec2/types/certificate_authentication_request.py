"""Generated from Smithy shape ``com.amazonaws.ec2#CertificateAuthenticationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CertificateAuthenticationRequest(TypedDict):
    client_root_certificate_chain_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in Certificate Manager (ACM).</p>"""
