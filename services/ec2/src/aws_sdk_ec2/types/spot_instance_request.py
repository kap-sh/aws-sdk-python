"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.instance_interruption_behavior
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.launch_specification
    import aws_sdk_ec2.types.ri_product_description
    import aws_sdk_ec2.types.spot_instance_state
    import aws_sdk_ec2.types.spot_instance_state_fault
    import aws_sdk_ec2.types.spot_instance_status
    import aws_sdk_ec2.types.spot_instance_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class SpotInstanceRequest(TypedDict):
    actual_block_hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Deprecated.</p>"""
    availability_zone_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone group. If you specify the same Availability Zone group for all Spot Instance requests, all Spot Instances are launched in the same Availability Zone.</p>"""
    block_duration_minutes: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Deprecated.</p>"""
    create_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time when the Spot Instance request was created, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
    fault: NotRequired[
        "aws_sdk_ec2.types.spot_instance_state_fault.SpotInstanceStateFault"
    ]
    """<p>The fault codes for the Spot Instance request, if any.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The instance ID, if an instance has been launched to fulfill the Spot Instance request.</p>"""
    launch_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance launch group. Launch groups are Spot Instances that launch together and terminate together.</p>"""
    launch_specification: NotRequired[
        "aws_sdk_ec2.types.launch_specification.LaunchSpecification"
    ]
    """<p>Additional information for launching instances.</p>"""
    launched_availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone in which the request is launched.</p> <p>Either <code>launchedAvailabilityZone</code> or <code>launchedAvailabilityZoneId</code> can be specified, but not both</p>"""
    launched_availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone in which the request is launched.</p> <p>Either <code>launchedAvailabilityZone</code> or <code>launchedAvailabilityZoneId</code> can be specified, but not both</p>"""
    product_description: NotRequired[
        "aws_sdk_ec2.types.ri_product_description.RIProductDescription"
    ]
    """<p>The product description associated with the Spot Instance.</p>"""
    spot_instance_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Instance request.</p>"""
    spot_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    state: NotRequired["aws_sdk_ec2.types.spot_instance_state.SpotInstanceState"]
    """<p>The state of the Spot Instance request. Spot request status information helps track your Spot Instance requests. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html\">Spot request status</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    status: NotRequired["aws_sdk_ec2.types.spot_instance_status.SpotInstanceStatus"]
    """<p>The status code and status message describing the Spot Instance request.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the resource.</p>"""
    type: NotRequired["aws_sdk_ec2.types.spot_instance_type.SpotInstanceType"]
    """<p>The Spot Instance request type.</p>"""
    valid_from: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The start date of the request, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). The request becomes active at this date and time.</p>"""
    valid_until: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The end date of the request, in UTC format (<i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p> <ul> <li> <p>For a persistent request, the request remains active until the <code>validUntil</code> date and time is reached. Otherwise, the request remains active until you cancel it. </p> </li> <li> <p>For a one-time request, the request remains active until all instances launch, the request is canceled, or the <code>validUntil</code> date and time is reached. By default, the request is valid for 7 days from the date the request was created.</p> </li> </ul>"""
    instance_interruption_behavior: NotRequired[
        "aws_sdk_ec2.types.instance_interruption_behavior.InstanceInterruptionBehavior"
    ]
    """<p>The behavior when a Spot Instance is interrupted.</p>"""
