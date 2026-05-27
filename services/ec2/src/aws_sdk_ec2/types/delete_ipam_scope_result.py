"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamScopeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_scope


class DeleteIpamScopeResult(TypedDict):
    ipam_scope: NotRequired["aws_sdk_ec2.types.ipam_scope.IpamScope"]
    """<p>Information about the results of the deletion.</p>"""
