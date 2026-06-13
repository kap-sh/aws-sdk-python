"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetResourcePermissionOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class GetResourcePermissionOutput(TypedDict):
    policy: NotRequired["str"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePermissionOutput) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetResourcePermissionOutput:
    out: GetResourcePermissionOutput = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
