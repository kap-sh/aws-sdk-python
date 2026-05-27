"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_interruption_behavior
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.request_spot_launch_specification
    import aws_sdk_ec2.types.spot_instance_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class RequestSpotInstancesRequest(TypedDict):
    launch_specification: NotRequired[
        "aws_sdk_ec2.types.request_spot_launch_specification.RequestSpotLaunchSpecification"
    ]
    """<p>The launch specification.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The key-value pair for tagging the Spot Instance request on creation. The value for <code>ResourceType</code> must be <code>spot-instances-request</code>, otherwise the Spot Instance request fails. To tag the Spot Instance request after it has been created, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html\">CreateTags</a>. </p>"""
    instance_interruption_behavior: NotRequired[
        "aws_sdk_ec2.types.instance_interruption_behavior.InstanceInterruptionBehavior"
    ]
    """<p>The behavior when a Spot Instance is interrupted. The default is <code>terminate</code>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of Spot Instances to launch.</p> <p>Default: 1</p>"""
    type: NotRequired["aws_sdk_ec2.types.spot_instance_type.SpotInstanceType"]
    """<p>The Spot Instance request type.</p> <p>Default: <code>one-time</code> </p>"""
    valid_from: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The start date of the request. If this is a one-time request, the request becomes active at this date and time and remains active until all instances launch, the request expires, or the request is canceled. If the request is persistent, the request becomes active at this date and time and remains active until it expires or is canceled.</p> <p>The specified start date and time cannot be equal to the current date and time. You must specify a start date and time that occurs after the current date and time.</p>"""
    valid_until: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The end date of the request, in UTC format (<i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p> <ul> <li> <p>For a persistent request, the request remains active until the <code>ValidUntil</code> date and time is reached. Otherwise, the request remains active until you cancel it. </p> </li> <li> <p>For a one-time request, the request remains active until all instances launch, the request is canceled, or the <code>ValidUntil</code> date and time is reached. By default, the request is valid for 7 days from the date the request was created.</p> </li> </ul>"""
    launch_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance launch group. Launch groups are Spot Instances that launch together and terminate together.</p> <p>Default: Instances are launched and terminated individually</p>"""
    availability_zone_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The user-specified name for a logical grouping of requests.</p> <p>When you specify an Availability Zone group in a Spot Instance request, all Spot Instances in the request are launched in the same Availability Zone. Instance proximity is maintained with this parameter, but the choice of Availability Zone is not. The group applies only to requests for Spot Instances of the same instance type. Any additional Spot Instance requests that are specified with the same Availability Zone group name are launched in that same Availability Zone, as long as at least one instance from the group is still active.</p> <p>If there is no active instance running in the Availability Zone group that you specify for a new Spot Instance request (all instances are terminated, the request is expired, or the maximum price you specified falls below current Spot price), then Amazon EC2 launches the instance in any Availability Zone where the constraint can be met. Consequently, the subsequent set of Spot Instances could be placed in a different zone from the original request, even if you specified the same Availability Zone group.</p> <p>Default: Instances are launched in any available Availability Zone.</p>"""
    block_duration_minutes: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Deprecated.</p>"""
