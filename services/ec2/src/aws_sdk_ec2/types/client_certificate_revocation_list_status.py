"""Generated from Smithy shape ``com.amazonaws.ec2#ClientCertificateRevocationListStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_certificate_revocation_list_status_code
    import aws_sdk_ec2.types.string


class ClientCertificateRevocationListStatus(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.client_certificate_revocation_list_status_code.ClientCertificateRevocationListStatusCode"
    ]
    """<p>The state of the client certificate revocation list.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message about the status of the client certificate revocation list, if applicable.</p>"""
