"""Generated from Smithy shape ``com.amazonaws.ecs#TotalLocalStorageGBRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_double


class TotalLocalStorageGBRequest(TypedDict):
    min: NotRequired["aws_sdk_ecs.types.boxed_double.BoxedDouble"]
    """<p>The minimum total local storage in GB. Instance types with less local storage are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_double.BoxedDouble"]
    """<p>The maximum total local storage in GB. Instance types with more local storage are excluded from selection.</p>"""
