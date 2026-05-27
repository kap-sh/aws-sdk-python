"""Generated from Smithy shape ``com.amazonaws.ec2#DestinationOptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.destination_file_format


class DestinationOptionsResponse(TypedDict):
    file_format: NotRequired[
        "aws_sdk_ec2.types.destination_file_format.DestinationFileFormat"
    ]
    """<p>The format for the flow log.</p>"""
    hive_compatible_partitions: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to use Hive-compatible prefixes for flow logs stored in Amazon S3.</p>"""
    per_hour_partition: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to partition the flow log per hour.</p>"""
