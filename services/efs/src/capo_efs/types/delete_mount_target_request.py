"""Generated from Smithy shape ``com.amazonaws.efs#DeleteMountTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_efs.types.mount_target_id


class DeleteMountTargetRequest(TypedDict, closed=True):
    mount_target_id: "capo_efs.types.mount_target_id.MountTargetId"
    """<p>The ID of the mount target to delete (String).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMountTargetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMountTargetRequest:
    out: DeleteMountTargetRequest = {}  # type: ignore[typeddict-item]
    return out
