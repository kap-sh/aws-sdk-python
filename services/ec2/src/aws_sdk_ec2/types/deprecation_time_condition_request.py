"""Generated from Smithy shape ``com.amazonaws.ec2#DeprecationTimeConditionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.maximum_days_since_deprecated_value


class DeprecationTimeConditionRequest(TypedDict):
    maximum_days_since_deprecated: NotRequired[
        "aws_sdk_ec2.types.maximum_days_since_deprecated_value.MaximumDaysSinceDeprecatedValue"
    ]
    """<p>The maximum number of days that have elapsed since the image was deprecated. Set to <code>0</code> to exclude all deprecated images.</p>"""
