"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSecondarySubnetResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_subnet
    import aws_sdk_ec2.types.string


class DeleteSecondarySubnetResult(TypedDict):
    secondary_subnet: NotRequired["aws_sdk_ec2.types.secondary_subnet.SecondarySubnet"]
    """<p>Information about the secondary subnet being deleted.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""
