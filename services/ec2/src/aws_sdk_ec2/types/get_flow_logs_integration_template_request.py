"""Generated from Smithy shape ``com.amazonaws.ec2#GetFlowLogsIntegrationTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integrate_services
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_flow_log_id


class GetFlowLogsIntegrationTemplateRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    flow_log_id: NotRequired["aws_sdk_ec2.types.vpc_flow_log_id.VpcFlowLogId"]
    """<p>The ID of the flow log.</p>"""
    config_delivery_s3_destination_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>To store the CloudFormation template in Amazon S3, specify the location in Amazon S3.</p>"""
    integrate_services: NotRequired[
        "aws_sdk_ec2.types.integrate_services.IntegrateServices"
    ]
    """<p>Information about the service integration.</p>"""
