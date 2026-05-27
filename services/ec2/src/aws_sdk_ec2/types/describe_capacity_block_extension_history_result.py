"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockExtensionHistoryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_extension_set
    import aws_sdk_ec2.types.string


class DescribeCapacityBlockExtensionHistoryResult(TypedDict):
    capacity_block_extensions: NotRequired[
        "aws_sdk_ec2.types.capacity_block_extension_set.CapacityBlockExtensionSet"
    ]
    """<p>Describes one or more of your Capacity Block extensions. The results describe only the Capacity Block extensions in the Amazon Web Services Region that you're currently using.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
