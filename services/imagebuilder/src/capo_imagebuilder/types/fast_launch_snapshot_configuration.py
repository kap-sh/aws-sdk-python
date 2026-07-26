"""Generated from Smithy shape ``com.amazonaws.imagebuilder#FastLaunchSnapshotConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.target_resource_count


class FastLaunchSnapshotConfiguration(TypedDict, closed=True):
    target_resource_count: NotRequired[
        "capo_imagebuilder.types.target_resource_count.TargetResourceCount"
    ]
    """<p>The number of pre-provisioned snapshots to keep on hand for a fast-launch enabled Windows AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FastLaunchSnapshotConfiguration) -> dict:
    out: dict = {}
    if "target_resource_count" in value:
        out["targetResourceCount"] = value["target_resource_count"]
    return out


def deserialize_json(data: dict) -> FastLaunchSnapshotConfiguration:
    out: FastLaunchSnapshotConfiguration = {}  # type: ignore[typeddict-item]
    if "targetResourceCount" in data:
        out["target_resource_count"] = data["targetResourceCount"]
    return out
