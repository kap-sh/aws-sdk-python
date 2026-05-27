"""Generated from Smithy shape ``com.amazonaws.ec2#FlowLog``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.destination_options_response
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.log_destination_type
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.traffic_type


class FlowLog(TypedDict):
    creation_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time the flow log was created.</p>"""
    deliver_logs_error_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Information about the error that occurred. <code>Rate limited</code> indicates that CloudWatch Logs throttling has been applied for one or more network interfaces, or that you've reached the limit on the number of log groups that you can create. <code>Access error</code> indicates that the IAM role associated with the flow log does not have sufficient permissions to publish to CloudWatch Logs. <code>Unknown error</code> indicates an internal error.</p>"""
    deliver_logs_permission_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the IAM role allows the service to publish logs to CloudWatch Logs.</p>"""
    deliver_cross_account_role: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the IAM role that allows the service to publish flow logs across accounts.</p>"""
    deliver_logs_status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the logs delivery (<code>SUCCESS</code> | <code>FAILED</code>).</p>"""
    flow_log_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the flow log.</p>"""
    flow_log_status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the flow log (<code>ACTIVE</code>).</p>"""
    log_group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the flow log group.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource being monitored.</p>"""
    traffic_type: NotRequired["aws_sdk_ec2.types.traffic_type.TrafficType"]
    """<p>The type of traffic captured for the flow log.</p>"""
    log_destination_type: NotRequired[
        "aws_sdk_ec2.types.log_destination_type.LogDestinationType"
    ]
    """<p>The type of destination for the flow log data.</p>"""
    log_destination: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the destination for the flow log data.</p>"""
    log_format: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The format of the flow log record.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the flow log.</p>"""
    max_aggregation_interval: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum interval of time, in seconds, during which a flow of packets is captured and aggregated into a flow log record.</p> <p>When a network interface is attached to a <a href=\"https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html\">Nitro-based instance</a>, the aggregation interval is always 60 seconds (1 minute) or less, regardless of the specified value.</p> <p>Valid Values: <code>60</code> | <code>600</code> </p>"""
    destination_options: NotRequired[
        "aws_sdk_ec2.types.destination_options_response.DestinationOptionsResponse"
    ]
    """<p>The destination options.</p>"""
