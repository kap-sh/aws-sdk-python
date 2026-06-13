"""Generated from Smithy shape ``com.amazonaws.quicksight#RecentSnapshotsConfigurations``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean


class RecentSnapshotsConfigurations(TypedDict):
    enabled: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>The recent snapshots configuration for an embedded Quick Sight dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecentSnapshotsConfigurations) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> RecentSnapshotsConfigurations:
    out: RecentSnapshotsConfigurations = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
