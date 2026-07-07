"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#PlatformCommand``."""

from typing_extensions import NotRequired, TypedDict


class PlatformCommand(TypedDict, closed=True):
    linux: NotRequired["str"]
    """<p>Command for Linux.</p>"""
    windows: NotRequired["str"]
    """<p>Command for Windows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlatformCommand) -> dict:
    out: dict = {}
    if "linux" in value:
        out["linux"] = value["linux"]
    if "windows" in value:
        out["windows"] = value["windows"]
    return out


def deserialize_json(data: dict) -> PlatformCommand:
    out: PlatformCommand = {}  # type: ignore[typeddict-item]
    if "linux" in data:
        out["linux"] = data["linux"]
    if "windows" in data:
        out["windows"] = data["windows"]
    return out
