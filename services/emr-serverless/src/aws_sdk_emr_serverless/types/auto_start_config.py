"""Generated from Smithy shape ``com.amazonaws.emrserverless#AutoStartConfig``."""

from typing_extensions import NotRequired, TypedDict


class AutoStartConfig(TypedDict, closed=True):
    enabled: NotRequired["bool"]
    """<p>Enables the application to automatically start on job submission. Defaults to true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoStartConfig) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> AutoStartConfig:
    out: AutoStartConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
