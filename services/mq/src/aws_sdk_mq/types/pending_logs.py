"""Generated from Smithy shape ``com.amazonaws.mq#PendingLogs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__boolean


class PendingLogs(TypedDict, closed=True):
    audit: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged.</p>"""
    general: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables general logging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PendingLogs) -> dict:
    out: dict = {}
    if "audit" in value:
        out["audit"] = value["audit"]
    if "general" in value:
        out["general"] = value["general"]
    return out


def deserialize_json(data: dict) -> PendingLogs:
    out: PendingLogs = {}  # type: ignore[typeddict-item]
    if "audit" in data:
        out["audit"] = data["audit"]
    if "general" in data:
        out["general"] = data["general"]
    return out
