"""Generated from Smithy shape ``com.amazonaws.lambda#CallbackOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.duration_seconds


class CallbackOptions(TypedDict, closed=True):
    timeout_seconds: "capo_lambda.types.duration_seconds.DurationSeconds"
    """<p>The timeout for the callback operation in seconds. If not specified or set to 0, the callback has no timeout.</p>"""
    heartbeat_timeout_seconds: "capo_lambda.types.duration_seconds.DurationSeconds"
    """<p>The heartbeat timeout for the callback operation, in seconds. If not specified or set to 0, heartbeat timeout is disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CallbackOptions) -> dict:
    out: dict = {}
    out["TimeoutSeconds"] = value.get("timeout_seconds", 0)
    out["HeartbeatTimeoutSeconds"] = value.get("heartbeat_timeout_seconds", 0)
    return out


def deserialize_json(data: dict) -> CallbackOptions:
    out: CallbackOptions = {}  # type: ignore[typeddict-item]
    if "TimeoutSeconds" in data:
        out["timeout_seconds"] = data["TimeoutSeconds"]
    else:
        out["timeout_seconds"] = 0
    if "HeartbeatTimeoutSeconds" in data:
        out["heartbeat_timeout_seconds"] = data["HeartbeatTimeoutSeconds"]
    else:
        out["heartbeat_timeout_seconds"] = 0
    return out
