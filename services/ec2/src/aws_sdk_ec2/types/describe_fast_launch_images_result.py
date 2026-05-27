"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastLaunchImagesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fast_launch_images_success_set
    import aws_sdk_ec2.types.next_token


class DescribeFastLaunchImagesResult(TypedDict):
    fast_launch_images: NotRequired[
        "aws_sdk_ec2.types.describe_fast_launch_images_success_set.DescribeFastLaunchImagesSuccessSet"
    ]
    """<p>A collection of details about the fast-launch enabled Windows images that meet the requested criteria.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
