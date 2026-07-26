"""Generated from Smithy shape ``com.amazonaws.iot#DeleteScheduledAuditRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.scheduled_audit_name


class DeleteScheduledAuditRequest(TypedDict, closed=True):
    scheduled_audit_name: "capo_iot.types.scheduled_audit_name.ScheduledAuditName"
    """<p>The name of the scheduled audit you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScheduledAuditRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteScheduledAuditRequest:
    out: DeleteScheduledAuditRequest = {}  # type: ignore[typeddict-item]
    return out
