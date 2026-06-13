"""Generated from Smithy shape ``com.amazonaws.datazone#DeploymentProperties``."""

from typing import TypedDict
from typing_extensions import NotRequired


class DeploymentProperties(TypedDict):
    start_timeout_minutes: NotRequired["int"]
    """<p>The start timeout of the environment blueprint deployment.</p>"""
    end_timeout_minutes: NotRequired["int"]
    """<p>The end timeout of the environment blueprint deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentProperties) -> dict:
    out: dict = {}
    if "start_timeout_minutes" in value:
        out["startTimeoutMinutes"] = value["start_timeout_minutes"]
    if "end_timeout_minutes" in value:
        out["endTimeoutMinutes"] = value["end_timeout_minutes"]
    return out


def deserialize_json(data: dict) -> DeploymentProperties:
    out: DeploymentProperties = {}  # type: ignore[typeddict-item]
    if "startTimeoutMinutes" in data:
        out["start_timeout_minutes"] = data["startTimeoutMinutes"]
    if "endTimeoutMinutes" in data:
        out["end_timeout_minutes"] = data["endTimeoutMinutes"]
    return out
