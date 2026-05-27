"""Generated from Smithy shape ``com.amazonaws.ec2#HibernationOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class HibernationOptionsRequest(TypedDict):
    configured: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Set to <code>true</code> to enable your instance for hibernation.</p> <p>For Spot Instances, if you set <code>Configured</code> to <code>true</code>, either omit the <code>InstanceInterruptionBehavior</code> parameter (for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotMarketOptions.html\"> <code>SpotMarketOptions</code> </a>), or set it to <code>hibernate</code>. When <code>Configured</code> is true:</p> <ul> <li> <p>If you omit <code>InstanceInterruptionBehavior</code>, it defaults to <code>hibernate</code>.</p> </li> <li> <p>If you set <code>InstanceInterruptionBehavior</code> to a value other than <code>hibernate</code>, you'll get an error.</p> </li> </ul> <p>Default: <code>false</code> </p>"""
