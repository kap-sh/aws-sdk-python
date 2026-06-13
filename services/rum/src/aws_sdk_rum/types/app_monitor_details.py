"""Generated from Smithy shape ``com.amazonaws.rum#AppMonitorDetails``."""

from typing import TypedDict

from typing_extensions import NotRequired


class AppMonitorDetails(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the app monitor.</p>"""
    id: NotRequired["str"]
    """<p>The unique ID of the app monitor.</p>"""
    version: NotRequired["str"]
    """<p>The version of the app monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppMonitorDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> AppMonitorDetails:
    out: AppMonitorDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "version" in data:
        out["version"] = data["version"]
    return out
