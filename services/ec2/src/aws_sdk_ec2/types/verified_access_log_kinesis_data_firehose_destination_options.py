"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogKinesisDataFirehoseDestinationOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class VerifiedAccessLogKinesisDataFirehoseDestinationOptions(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether logging is enabled.</p>"""
    delivery_stream: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the delivery stream.</p>"""
