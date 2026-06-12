"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CreateVolumeResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.volume_id

class CreateVolumeResponse(TypedDict):
    volume_id: NotRequired["aws_sdk_workspaces_instances.types.volume_id.VolumeId"]
    """<p>Unique identifier for the new volume.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVolumeResponse) -> dict:
    out: dict = {}
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVolumeResponse:
    out: CreateVolumeResponse = {}  # type: ignore[typeddict-item]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    return out