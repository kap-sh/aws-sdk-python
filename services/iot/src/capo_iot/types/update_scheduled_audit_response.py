"""Generated from Smithy shape ``com.amazonaws.iot#UpdateScheduledAuditResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.scheduled_audit_arn


class UpdateScheduledAuditResponse(TypedDict, closed=True):
    scheduled_audit_arn: NotRequired[
        "capo_iot.types.scheduled_audit_arn.ScheduledAuditArn"
    ]
    """<p>The ARN of the scheduled audit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScheduledAuditResponse) -> dict:
    out: dict = {}
    if "scheduled_audit_arn" in value:
        out["scheduledAuditArn"] = value["scheduled_audit_arn"]
    return out


def deserialize_json(data: dict) -> UpdateScheduledAuditResponse:
    out: UpdateScheduledAuditResponse = {}  # type: ignore[typeddict-item]
    if "scheduledAuditArn" in data:
        out["scheduled_audit_arn"] = data["scheduledAuditArn"]
    return out
