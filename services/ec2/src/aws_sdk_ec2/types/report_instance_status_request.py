"""Generated from Smithy shape ``com.amazonaws.ec2#ReportInstanceStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_id_string_list
    import aws_sdk_ec2.types.reason_codes_list
    import aws_sdk_ec2.types.report_instance_status_request_description
    import aws_sdk_ec2.types.report_status_type


class ReportInstanceStatusRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instances: NotRequired[
        "aws_sdk_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The instances.</p>"""
    status: NotRequired["aws_sdk_ec2.types.report_status_type.ReportStatusType"]
    """<p>The status of all instances listed.</p>"""
    start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time at which the reported instance health state began.</p>"""
    end_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time at which the reported instance health state ended.</p>"""
    reason_codes: NotRequired["aws_sdk_ec2.types.reason_codes_list.ReasonCodesList"]
    """<p>The reason codes that describe the health state of your instance.</p> <ul> <li> <p> <code>instance-stuck-in-state</code>: My instance is stuck in a state.</p> </li> <li> <p> <code>unresponsive</code>: My instance is unresponsive.</p> </li> <li> <p> <code>not-accepting-credentials</code>: My instance is not accepting my credentials.</p> </li> <li> <p> <code>password-not-available</code>: A password is not available for my instance.</p> </li> <li> <p> <code>performance-network</code>: My instance is experiencing performance problems that I believe are network related.</p> </li> <li> <p> <code>performance-instance-store</code>: My instance is experiencing performance problems that I believe are related to the instance stores.</p> </li> <li> <p> <code>performance-ebs-volume</code>: My instance is experiencing performance problems that I believe are related to an EBS volume.</p> </li> <li> <p> <code>performance-other</code>: My instance is experiencing performance problems.</p> </li> <li> <p> <code>other</code>: [explain using the description parameter]</p> </li> </ul>"""
    description: NotRequired[
        "aws_sdk_ec2.types.report_instance_status_request_description.ReportInstanceStatusRequestDescription"
    ]
    """<p>Descriptive text about the health state of your instance.</p>"""
