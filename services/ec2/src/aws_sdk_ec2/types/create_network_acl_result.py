"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkAclResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_acl
    import aws_sdk_ec2.types.string


class CreateNetworkAclResult(TypedDict):
    network_acl: NotRequired["aws_sdk_ec2.types.network_acl.NetworkAcl"]
    """<p>Information about the network ACL.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""
