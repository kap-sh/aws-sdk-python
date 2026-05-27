"""Generated from Smithy shape ``com.amazonaws.ec2#ClientRouteEnforcementOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class ClientRouteEnforcementOptions(TypedDict):
    enforced: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Enable or disable Client Route Enforcement. The state can either be <code>true</code> (enabled) or <code>false</code> (disabled). The default is <code>false</code>.</p> <p>Valid values: <code>true | false</code> </p> <p>Default value: <code>false</code> </p>"""
