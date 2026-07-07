"""Generated from Smithy shape ``com.amazonaws.iot#DescribeScheduledAuditRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.scheduled_audit_name


class DescribeScheduledAuditRequest(TypedDict, closed=True):
    scheduled_audit_name: "aws_sdk_iot.types.scheduled_audit_name.ScheduledAuditName"
    """<p>The name of the scheduled audit whose information you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeScheduledAuditRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeScheduledAuditRequest:
    out: DescribeScheduledAuditRequest = {}  # type: ignore[typeddict-item]
    return out
