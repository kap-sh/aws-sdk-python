"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorCountRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer


class AcceleratorCountRequest(TypedDict):
    min: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The minimum number of accelerators. Instance types with fewer accelerators are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of accelerators. Instance types with more accelerators are excluded from selection.</p>"""
