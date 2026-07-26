"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergSnapshotManagementSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.positive_integer


class IcebergSnapshotManagementSettings(TypedDict, closed=True):
    min_snapshots_to_keep: NotRequired[
        "capo_s3tables.types.positive_integer.PositiveInteger"
    ]
    """<p>The minimum number of snapshots to keep.</p>"""
    max_snapshot_age_hours: NotRequired[
        "capo_s3tables.types.positive_integer.PositiveInteger"
    ]
    """<p>The maximum age of a snapshot before it can be expired.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergSnapshotManagementSettings) -> dict:
    out: dict = {}
    if "min_snapshots_to_keep" in value:
        out["minSnapshotsToKeep"] = value["min_snapshots_to_keep"]
    if "max_snapshot_age_hours" in value:
        out["maxSnapshotAgeHours"] = value["max_snapshot_age_hours"]
    return out


def deserialize_json(data: dict) -> IcebergSnapshotManagementSettings:
    out: IcebergSnapshotManagementSettings = {}  # type: ignore[typeddict-item]
    if "minSnapshotsToKeep" in data:
        out["min_snapshots_to_keep"] = data["minSnapshotsToKeep"]
    if "maxSnapshotAgeHours" in data:
        out["max_snapshot_age_hours"] = data["maxSnapshotAgeHours"]
    return out
