"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcBlockPublicAccessExclusionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion_id


class DeleteVpcBlockPublicAccessExclusionRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    exclusion_id: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_exclusion_id.VpcBlockPublicAccessExclusionId"
    ]
    """<p>The ID of the exclusion.</p>"""
