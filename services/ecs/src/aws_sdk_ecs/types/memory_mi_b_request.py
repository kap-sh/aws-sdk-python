"""Generated from Smithy shape ``com.amazonaws.ecs#MemoryMiBRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer


class MemoryMiBRequest(TypedDict):
    min: "aws_sdk_ecs.types.boxed_integer.BoxedInteger"
    """<p>The minimum amount of memory in MiB. Instance types with less memory than this value are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum amount of memory in MiB. Instance types with more memory than this value are excluded from selection.</p>"""
