"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#QuickSetupTypeOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class QuickSetupTypeOutput(TypedDict):
    type: NotRequired["str"]
    """<p>The type of the Quick Setup configuration.</p>"""
    latest_version: NotRequired["str"]
    """<p>The latest version number of the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickSetupTypeOutput) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "latest_version" in value:
        out["LatestVersion"] = value["latest_version"]
    return out


def deserialize_json(data: dict) -> QuickSetupTypeOutput:
    out: QuickSetupTypeOutput = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "LatestVersion" in data:
        out["latest_version"] = data["LatestVersion"]
    return out
