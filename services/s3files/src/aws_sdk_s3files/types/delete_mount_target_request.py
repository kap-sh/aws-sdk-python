"""Generated from Smithy shape ``com.amazonaws.s3files#DeleteMountTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3files.types.mount_target_id


class DeleteMountTargetRequest(TypedDict):
    mount_target_id: "aws_sdk_s3files.types.mount_target_id.MountTargetId"
    """<p>The ID of the mount target to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMountTargetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMountTargetRequest:
    out: DeleteMountTargetRequest = {}  # type: ignore[typeddict-item]
    return out
