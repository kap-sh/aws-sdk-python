"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSecondaryNetworkResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_network
    import aws_sdk_ec2.types.string


class DeleteSecondaryNetworkResult(TypedDict):
    secondary_network: NotRequired[
        "aws_sdk_ec2.types.secondary_network.SecondaryNetwork"
    ]
    """<p>Information about the secondary network.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""
