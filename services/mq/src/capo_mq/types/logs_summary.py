"""Generated from Smithy shape ``com.amazonaws.mq#LogsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__boolean
    import capo_mq.types.__string
    import capo_mq.types.pending_logs


class LogsSummary(TypedDict, closed=True):
    audit: NotRequired["capo_mq.types.__boolean.__boolean"]
    """<p>Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged.</p>"""
    audit_log_group: NotRequired["capo_mq.types.__string.__string"]
    """<p>The location of the CloudWatch Logs log group where audit logs are sent.</p>"""
    general: NotRequired["capo_mq.types.__boolean.__boolean"]
    """<p>Enables general logging.</p>"""
    general_log_group: NotRequired["capo_mq.types.__string.__string"]
    """<p>The location of the CloudWatch Logs log group where general logs are sent.</p>"""
    pending: NotRequired["capo_mq.types.pending_logs.PendingLogs"]
    """<p>The list of information about logs pending to be deployed for the specified broker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogsSummary) -> dict:
    out: dict = {}
    if "audit" in value:
        out["audit"] = value["audit"]
    if "audit_log_group" in value:
        out["auditLogGroup"] = value["audit_log_group"]
    if "general" in value:
        out["general"] = value["general"]
    if "general_log_group" in value:
        out["generalLogGroup"] = value["general_log_group"]
    if "pending" in value:
        import capo_mq.types.pending_logs

        out["pending"] = capo_mq.types.pending_logs.serialize_json(value["pending"])
    return out


def deserialize_json(data: dict) -> LogsSummary:
    out: LogsSummary = {}  # type: ignore[typeddict-item]
    if "audit" in data:
        out["audit"] = data["audit"]
    if "auditLogGroup" in data:
        out["audit_log_group"] = data["auditLogGroup"]
    if "general" in data:
        out["general"] = data["general"]
    if "generalLogGroup" in data:
        out["general_log_group"] = data["generalLogGroup"]
    if "pending" in data:
        import capo_mq.types.pending_logs

        out["pending"] = capo_mq.types.pending_logs.deserialize_json(data["pending"])
    return out
