"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFlowLogsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.destination_options_request
    import aws_sdk_ec2.types.flow_log_resource_ids
    import aws_sdk_ec2.types.flow_logs_resource_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.log_destination_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.traffic_type


class CreateFlowLogsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""
    deliver_logs_permission_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the IAM role that allows Amazon EC2 to publish flow logs to the log destination.</p> <p>This parameter is required if the destination type is <code>cloud-watch-logs</code>, or if the destination type is <code>kinesis-data-firehose</code> and the delivery stream and the resources to monitor are in different accounts.</p>"""
    deliver_cross_account_role: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts.</p>"""
    log_group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs.</p> <p>This parameter is valid only if the destination type is <code>cloud-watch-logs</code>.</p>"""
    resource_ids: NotRequired[
        "aws_sdk_ec2.types.flow_log_resource_ids.FlowLogResourceIds"
    ]
    """<p>The IDs of the resources to monitor. For example, if the resource type is <code>VPC</code>, specify the IDs of the VPCs.</p> <p>Constraints: Maximum of 25 for transit gateway resource types. Maximum of 1000 for the other resource types.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.flow_logs_resource_type.FlowLogsResourceType"
    ]
    """<p>The type of resource to monitor.</p>"""
    traffic_type: NotRequired["aws_sdk_ec2.types.traffic_type.TrafficType"]
    """<p>The type of traffic to monitor (accepted traffic, rejected traffic, or all traffic). This parameter is not supported for transit gateway resource types. It is required for the other resource types.</p>"""
    log_destination_type: NotRequired[
        "aws_sdk_ec2.types.log_destination_type.LogDestinationType"
    ]
    """<p>The type of destination for the flow log data.</p> <p>Default: <code>cloud-watch-logs</code> </p>"""
    log_destination: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination for the flow log data. The meaning of this parameter depends on the destination type.</p> <ul> <li> <p>If the destination type is <code>cloud-watch-logs</code>, specify the ARN of a CloudWatch Logs log group. For example:</p> <p>arn:aws:logs:<i>region</i>:<i>account_id</i>:log-group:<i>my_group</i> </p> <p>Alternatively, use the <code>LogGroupName</code> parameter.</p> </li> <li> <p>If the destination type is <code>s3</code>, specify the ARN of an S3 bucket. For example:</p> <p>arn:aws:s3:::<i>my_bucket</i>/<i>my_subfolder</i>/</p> <p>The subfolder is optional. Note that you can't use <code>AWSLogs</code> as a subfolder name.</p> </li> <li> <p>If the destination type is <code>kinesis-data-firehose</code>, specify the ARN of a Kinesis Data Firehose delivery stream. For example:</p> <p>arn:aws:firehose:<i>region</i>:<i>account_id</i>:deliverystream:<i>my_stream</i> </p> </li> </ul>"""
    log_format: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The fields to include in the flow log record. List the fields in the order in which they should appear. If you omit this parameter, the flow log is created using the default format. If you specify this parameter, you must include at least one field. For more information about the available fields, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html\">Flow log records</a> in the <i>Amazon VPC User Guide</i> or <a href=\"https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html#flow-log-records\">Transit Gateway Flow Log records</a> in the <i>Amazon Web Services Transit Gateway Guide</i>.</p> <p>Specify the fields using the <code>${field-id}</code> format, separated by spaces.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the flow logs.</p>"""
    max_aggregation_interval: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. The possible values are 60 seconds (1 minute) or 600 seconds (10 minutes). This parameter must be 60 seconds for transit gateway resource types.</p> <p>When a network interface is attached to a <a href=\"https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html\">Nitro-based instance</a>, the aggregation interval is always 60 seconds or less, regardless of the value that you specify.</p> <p>Default: 600</p>"""
    destination_options: NotRequired[
        "aws_sdk_ec2.types.destination_options_request.DestinationOptionsRequest"
    ]
    """<p>The destination options.</p>"""
