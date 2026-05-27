"""Generated from Smithy shape ``com.amazonaws.ec2#CloudWatchLogOptionsSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.cloud_watch_log_group_arn
    import aws_sdk_ec2.types.string


class CloudWatchLogOptionsSpecification(TypedDict):
    log_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Enable or disable VPN tunnel logging feature. Default value is <code>False</code>.</p> <p>Valid values: <code>True</code> | <code>False</code> </p>"""
    log_group_arn: NotRequired[
        "aws_sdk_ec2.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch log group to send logs to.</p>"""
    log_output_format: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Set log format. Default format is <code>json</code>.</p> <p>Valid values: <code>json</code> | <code>text</code> </p>"""
    bgp_log_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to enable BGP logging for the VPN connection. Default value is <code>False</code>.</p> <p>Valid values: <code>True</code> | <code>False</code> </p>"""
    bgp_log_group_arn: NotRequired[
        "aws_sdk_ec2.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch log group where BGP logs will be sent.</p>"""
    bgp_log_output_format: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The desired output format for BGP logs to be sent to CloudWatch. Default format is <code>json</code>.</p> <p>Valid values: <code>json</code> | <code>text</code> </p>"""
