"""Generated from Smithy shape ``com.amazonaws.ecs#VCpuCountRangeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer


class VCpuCountRangeRequest(TypedDict):
    min: "aws_sdk_ecs.types.boxed_integer.BoxedInteger"
    """<p>The minimum number of vCPUs. Instance types with fewer vCPUs than this value are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of vCPUs. Instance types with more vCPUs than this value are excluded from selection.</p>"""
