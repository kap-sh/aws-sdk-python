"""Generated from Smithy shape ``com.amazonaws.emrserverless#AutoStopConfig``."""

from typing import TypedDict

from typing_extensions import NotRequired


class AutoStopConfig(TypedDict):
    enabled: NotRequired["bool"]
    """<p>Enables the application to automatically stop after a certain amount of time being idle. Defaults to true.</p>"""
    idle_timeout_minutes: NotRequired["int"]
    """<p>The amount of idle time in minutes after which your application will automatically stop. Defaults to 15 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoStopConfig) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "idle_timeout_minutes" in value:
        out["idleTimeoutMinutes"] = value["idle_timeout_minutes"]
    return out


def deserialize_json(data: dict) -> AutoStopConfig:
    out: AutoStopConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "idleTimeoutMinutes" in data:
        out["idle_timeout_minutes"] = data["idleTimeoutMinutes"]
    return out
