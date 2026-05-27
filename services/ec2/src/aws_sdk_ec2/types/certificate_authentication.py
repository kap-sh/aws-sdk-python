"""Generated from Smithy shape ``com.amazonaws.ec2#CertificateAuthentication``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CertificateAuthentication(TypedDict):
    client_root_certificate_chain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the client certificate. </p>"""
