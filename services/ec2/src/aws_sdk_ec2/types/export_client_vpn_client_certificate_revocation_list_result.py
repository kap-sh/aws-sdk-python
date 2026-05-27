"""Generated from Smithy shape ``com.amazonaws.ec2#ExportClientVpnClientCertificateRevocationListResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_certificate_revocation_list_status
    import aws_sdk_ec2.types.string


class ExportClientVpnClientCertificateRevocationListResult(TypedDict):
    certificate_revocation_list: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Information about the client certificate revocation list.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.client_certificate_revocation_list_status.ClientCertificateRevocationListStatus"
    ]
    """<p>The current state of the client certificate revocation list.</p>"""
