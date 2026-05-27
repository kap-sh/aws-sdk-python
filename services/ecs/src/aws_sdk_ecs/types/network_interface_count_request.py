"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkInterfaceCountRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer


class NetworkInterfaceCountRequest(TypedDict):
    min: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The minimum number of network interfaces. Instance types that support fewer network interfaces are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of network interfaces. Instance types that support more network interfaces are excluded from selection.</p>"""
