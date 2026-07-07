"""Generated from Smithy shape ``com.amazonaws.iot#CreateScheduledAuditResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.scheduled_audit_arn


class CreateScheduledAuditResponse(TypedDict, closed=True):
    scheduled_audit_arn: NotRequired[
        "aws_sdk_iot.types.scheduled_audit_arn.ScheduledAuditArn"
    ]
    """<p>The ARN of the scheduled audit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScheduledAuditResponse) -> dict:
    out: dict = {}
    if "scheduled_audit_arn" in value:
        out["scheduledAuditArn"] = value["scheduled_audit_arn"]
    return out


def deserialize_json(data: dict) -> CreateScheduledAuditResponse:
    out: CreateScheduledAuditResponse = {}  # type: ignore[typeddict-item]
    if "scheduledAuditArn" in data:
        out["scheduled_audit_arn"] = data["scheduledAuditArn"]
    return out
