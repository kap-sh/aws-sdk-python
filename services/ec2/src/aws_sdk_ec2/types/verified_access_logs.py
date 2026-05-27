"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogs``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_log_cloud_watch_logs_destination
    import aws_sdk_ec2.types.verified_access_log_kinesis_data_firehose_destination
    import aws_sdk_ec2.types.verified_access_log_s3_destination


class VerifiedAccessLogs(TypedDict):
    s3: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_s3_destination.VerifiedAccessLogS3Destination"
    ]
    """<p>Amazon S3 logging options.</p>"""
    cloud_watch_logs: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_cloud_watch_logs_destination.VerifiedAccessLogCloudWatchLogsDestination"
    ]
    """<p>CloudWatch Logs logging destination.</p>"""
    kinesis_data_firehose: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_kinesis_data_firehose_destination.VerifiedAccessLogKinesisDataFirehoseDestination"
    ]
    """<p>Kinesis logging destination.</p>"""
    log_version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The log version.</p>"""
    include_trust_context: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether trust data is included in the logs.</p>"""
