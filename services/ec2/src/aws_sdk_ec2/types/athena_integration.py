"""Generated from Smithy shape ``com.amazonaws.ec2#AthenaIntegration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.partition_load_frequency
    import aws_sdk_ec2.types.string


class AthenaIntegration(TypedDict):
    integration_result_s3_destination_arn: NotRequired[
        "aws_sdk_ec2.types.string.String"
    ]
    """<p>The location in Amazon S3 to store the generated CloudFormation template.</p>"""
    partition_load_frequency: NotRequired[
        "aws_sdk_ec2.types.partition_load_frequency.PartitionLoadFrequency"
    ]
    """<p>The schedule for adding new partitions to the table.</p>"""
    partition_start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date for the partition.</p>"""
    partition_end_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The end date for the partition.</p>"""
