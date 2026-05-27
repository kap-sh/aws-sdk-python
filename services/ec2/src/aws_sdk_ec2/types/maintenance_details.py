"""Generated from Smithy shape ``com.amazonaws.ec2#MaintenanceDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class MaintenanceDetails(TypedDict):
    pending_maintenance: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Verify existence of a pending maintenance.</p>"""
    maintenance_auto_applied_after: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The timestamp after which Amazon Web Services will automatically apply maintenance.</p>"""
    last_maintenance_applied: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Timestamp of last applied maintenance.</p>"""
