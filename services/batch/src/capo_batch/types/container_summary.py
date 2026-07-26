"""Generated from Smithy shape ``com.amazonaws.batch#ContainerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.string


class ContainerSummary(TypedDict, closed=True):
    exit_code: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The exit code to return upon completion.</p>"""
    reason: NotRequired["capo_batch.types.string.String"]
    """<p>A short (255 max characters) human-readable string to provide additional details for a running or stopped container.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerSummary) -> dict:
    out: dict = {}
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ContainerSummary:
    out: ContainerSummary = {}  # type: ignore[typeddict-item]
    if "exitCode" in data:
        out["exit_code"] = data["exitCode"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
