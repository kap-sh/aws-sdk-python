"""Generated from Smithy shape ``com.amazonaws.efs#DescribeMountTargetSecurityGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_efs.types.mount_target_id


class DescribeMountTargetSecurityGroupsRequest(TypedDict, closed=True):
    mount_target_id: "capo_efs.types.mount_target_id.MountTargetId"
    """<p>The ID of the mount target whose security groups you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMountTargetSecurityGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeMountTargetSecurityGroupsRequest:
    out: DescribeMountTargetSecurityGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
