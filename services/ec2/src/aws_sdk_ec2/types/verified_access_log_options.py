"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_log_cloud_watch_logs_destination_options
    import aws_sdk_ec2.types.verified_access_log_kinesis_data_firehose_destination_options
    import aws_sdk_ec2.types.verified_access_log_s3_destination_options


class VerifiedAccessLogOptions(TypedDict):
    s3: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_s3_destination_options.VerifiedAccessLogS3DestinationOptions"
    ]
    """<p>Sends Verified Access logs to Amazon S3.</p>"""
    cloud_watch_logs: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_cloud_watch_logs_destination_options.VerifiedAccessLogCloudWatchLogsDestinationOptions"
    ]
    """<p>Sends Verified Access logs to CloudWatch Logs.</p>"""
    kinesis_data_firehose: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_kinesis_data_firehose_destination_options.VerifiedAccessLogKinesisDataFirehoseDestinationOptions"
    ]
    """<p>Sends Verified Access logs to Kinesis.</p>"""
    log_version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The logging version.</p> <p>Valid values: <code>ocsf-0.1</code> | <code>ocsf-1.0.0-rc.2</code> </p>"""
    include_trust_context: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to include trust data sent by trust providers in the logs.</p>"""
