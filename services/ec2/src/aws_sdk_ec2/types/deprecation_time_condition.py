"""Generated from Smithy shape ``com.amazonaws.ec2#DeprecationTimeCondition``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.maximum_days_since_deprecated_value


class DeprecationTimeCondition(TypedDict):
    maximum_days_since_deprecated: NotRequired[
        "aws_sdk_ec2.types.maximum_days_since_deprecated_value.MaximumDaysSinceDeprecatedValue"
    ]
    """<p>The maximum number of days that have elapsed since the image was deprecated. When set to <code>0</code>, no deprecated images are allowed.</p>"""
