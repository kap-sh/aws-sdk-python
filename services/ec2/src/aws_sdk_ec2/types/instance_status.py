"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.ebs_status_summary
    import aws_sdk_ec2.types.instance_state
    import aws_sdk_ec2.types.instance_status_event_list
    import aws_sdk_ec2.types.instance_status_summary
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.string


class InstanceStatus(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone of the instance.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone of the instance.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the instance.</p>"""
    events: NotRequired[
        "aws_sdk_ec2.types.instance_status_event_list.InstanceStatusEventList"
    ]
    """<p>Any scheduled events associated with the instance.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    instance_state: NotRequired["aws_sdk_ec2.types.instance_state.InstanceState"]
    """<p>The intended state of the instance. <a>DescribeInstanceStatus</a> requires that an instance be in the <code>running</code> state.</p>"""
    instance_status: NotRequired[
        "aws_sdk_ec2.types.instance_status_summary.InstanceStatusSummary"
    ]
    """<p>Reports impaired functionality that stems from issues internal to the instance, such as impaired reachability.</p>"""
    system_status: NotRequired[
        "aws_sdk_ec2.types.instance_status_summary.InstanceStatusSummary"
    ]
    """<p>Reports impaired functionality that stems from issues related to the systems that support an instance, such as hardware failures and network connectivity problems.</p>"""
    attached_ebs_status: NotRequired[
        "aws_sdk_ec2.types.ebs_status_summary.EbsStatusSummary"
    ]
    """<p>Reports impaired functionality that stems from an attached Amazon EBS volume that is unreachable and unable to complete I/O operations.</p>"""
