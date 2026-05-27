"""Generated from Smithy shape ``com.amazonaws.ec2#SpotMarketOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_interruption_behavior
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.spot_instance_type
    import aws_sdk_ec2.types.string


class SpotMarketOptions(TypedDict):
    max_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum hourly price that you're willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your Spot Instances will be interrupted more frequently than if you do not specify this parameter.</p> <p>If you specify a maximum price, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an <code>InvalidParameterValue</code> error message.</p> </important>"""
    spot_instance_type: NotRequired[
        "aws_sdk_ec2.types.spot_instance_type.SpotInstanceType"
    ]
    """<p>The Spot Instance request type. For <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances\">RunInstances</a>, persistent Spot Instance requests are only supported when the instance interruption behavior is either <code>hibernate</code> or <code>stop</code>.</p>"""
    block_duration_minutes: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Deprecated.</p>"""
    valid_until: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The end date of the request, in UTC format (<i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). Supported only for persistent requests.</p> <ul> <li> <p>For a persistent request, the request remains active until the <code>ValidUntil</code> date and time is reached. Otherwise, the request remains active until you cancel it.</p> </li> <li> <p>For a one-time request, <code>ValidUntil</code> is not supported. The request remains active until all instances launch or you cancel the request.</p> </li> </ul>"""
    instance_interruption_behavior: NotRequired[
        "aws_sdk_ec2.types.instance_interruption_behavior.InstanceInterruptionBehavior"
    ]
    """<p>The behavior when a Spot Instance is interrupted.</p> <p>If <code>Configured</code> (for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest.html\"> <code>HibernationOptions</code> </a>) is set to <code>true</code>, the <code>InstanceInterruptionBehavior</code> parameter is automatically set to <code>hibernate</code>. If you set it to <code>stop</code> or <code>terminate</code>, you'll get an error.</p> <p>If <code>Configured</code> (for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest.html\"> <code>HibernationOptions</code> </a>) is set to <code>false</code> or <code>null</code>, the <code>InstanceInterruptionBehavior</code> parameter is automatically set to <code>terminate</code>. You can also set it to <code>stop</code> or <code>hibernate</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruption-behavior.html\">Interruption behavior</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
