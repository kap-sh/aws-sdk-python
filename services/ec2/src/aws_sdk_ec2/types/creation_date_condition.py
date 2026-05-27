"""Generated from Smithy shape ``com.amazonaws.ec2#CreationDateCondition``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.maximum_days_since_created_value


class CreationDateCondition(TypedDict):
    maximum_days_since_created: NotRequired[
        "aws_sdk_ec2.types.maximum_days_since_created_value.MaximumDaysSinceCreatedValue"
    ]
    """<p>The maximum number of days that have elapsed since the image was created. For example, a value of <code>300</code> allows images that were created within the last 300 days.</p>"""
