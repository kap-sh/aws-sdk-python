"""Generated from Smithy shape ``com.amazonaws.configservice#DeliverConfigSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.string


class DeliverConfigSnapshotResponse(TypedDict, closed=True):
    config_snapshot_id: NotRequired["capo_config_service.types.string.String"]
    """<p>The ID of the snapshot that is being created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverConfigSnapshotResponse) -> dict:
    out: dict = {}
    if "config_snapshot_id" in value:
        out["configSnapshotId"] = value["config_snapshot_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliverConfigSnapshotResponse:
    out: DeliverConfigSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "configSnapshotId" in data:
        out["config_snapshot_id"] = data["configSnapshotId"]
    return out
