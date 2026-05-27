"""Generated from Smithy shape ``com.amazonaws.ec2#ClientRouteEnforcementResponseOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class ClientRouteEnforcementResponseOptions(TypedDict):
    enforced: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Status of the client route enforcement feature, indicating whether Client Route Enforcement is <code>true</code> (enabled) or <code>false</code> (disabled).</p> <p>Valid values: <code>true | false</code> </p> <p>Default value: <code>false</code> </p>"""
