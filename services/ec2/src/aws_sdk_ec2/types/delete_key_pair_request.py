"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteKeyPairRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.key_pair_id
    import aws_sdk_ec2.types.key_pair_name_with_resolver


class DeleteKeyPairRequest(TypedDict):
    key_name: NotRequired[
        "aws_sdk_ec2.types.key_pair_name_with_resolver.KeyPairNameWithResolver"
    ]
    """<p>The name of the key pair.</p>"""
    key_pair_id: NotRequired["aws_sdk_ec2.types.key_pair_id.KeyPairId"]
    """<p>The ID of the key pair.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
