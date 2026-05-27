"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateSpotMarketOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_interruption_behavior
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.spot_instance_type
    import aws_sdk_ec2.types.string


class LaunchTemplateSpotMarketOptionsRequest(TypedDict):
    max_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum hourly price you're willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price. If you do specify this parameter, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an <code>InvalidParameterValue</code> error message when the launch template is used to launch an instance.</p> <important> <p>If you specify a maximum price, your Spot Instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    spot_instance_type: NotRequired[
        "aws_sdk_ec2.types.spot_instance_type.SpotInstanceType"
    ]
    """<p>The Spot Instance request type.</p>"""
    block_duration_minutes: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Deprecated.</p>"""
    valid_until: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The end date of the request, in UTC format (<i>YYYY-MM-DD</i>T<i>HH:MM:SS</i>Z). Supported only for persistent requests.</p> <ul> <li> <p>For a persistent request, the request remains active until the <code>ValidUntil</code> date and time is reached. Otherwise, the request remains active until you cancel it.</p> </li> <li> <p>For a one-time request, <code>ValidUntil</code> is not supported. The request remains active until all instances launch or you cancel the request.</p> </li> </ul> <p>Default: 7 days from the current date</p>"""
    instance_interruption_behavior: NotRequired[
        "aws_sdk_ec2.types.instance_interruption_behavior.InstanceInterruptionBehavior"
    ]
    """<p>The behavior when a Spot Instance is interrupted. The default is <code>terminate</code>.</p>"""
