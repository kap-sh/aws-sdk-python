"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatsDetectedItemCount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer


class ThreatsDetectedItemCount(TypedDict):
    files: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>Total number of infected files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatsDetectedItemCount) -> dict:
    out: dict = {}
    if "files" in value:
        out["files"] = value["files"]
    return out


def deserialize_json(data: dict) -> ThreatsDetectedItemCount:
    out: ThreatsDetectedItemCount = {}  # type: ignore[typeddict-item]
    if "files" in data:
        out["files"] = data["files"]
    return out
