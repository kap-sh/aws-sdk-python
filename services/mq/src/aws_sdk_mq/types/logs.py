"""Generated from Smithy shape ``com.amazonaws.mq#Logs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__boolean


class Logs(TypedDict, closed=True):
    audit: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. Does not apply to RabbitMQ brokers.</p>"""
    general: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables general logging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Logs) -> dict:
    out: dict = {}
    if "audit" in value:
        out["audit"] = value["audit"]
    if "general" in value:
        out["general"] = value["general"]
    return out


def deserialize_json(data: dict) -> Logs:
    out: Logs = {}  # type: ignore[typeddict-item]
    if "audit" in data:
        out["audit"] = data["audit"]
    if "general" in data:
        out["general"] = data["general"]
    return out
