"""Generated from Smithy shape ``com.amazonaws.guardduty#AutonomousSystem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.string


class AutonomousSystem(TypedDict):
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Name associated with the Autonomous System (AS).</p>"""
    number: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The unique number that identifies the Autonomous System (AS).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutonomousSystem) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "number" in value:
        out["number"] = value["number"]
    return out


def deserialize_json(data: dict) -> AutonomousSystem:
    out: AutonomousSystem = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "number" in data:
        out["number"] = data["number"]
    return out
