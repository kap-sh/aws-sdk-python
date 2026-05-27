"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSpotDatafeedSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class CreateSpotDatafeedSubscriptionRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket in which to store the Spot Instance data feed. For more information about bucket names, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html\">Bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix for the data feed file names.</p>"""
