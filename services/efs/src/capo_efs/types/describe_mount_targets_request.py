"""Generated from Smithy shape ``com.amazonaws.efs#DescribeMountTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.access_point_id
    import capo_efs.types.file_system_id
    import capo_efs.types.marker
    import capo_efs.types.max_items
    import capo_efs.types.mount_target_id


class DescribeMountTargetsRequest(TypedDict, closed=True):
    max_items: NotRequired["capo_efs.types.max_items.MaxItems"]
    """<p>(Optional) Maximum number of mount targets to return in the response. Currently, this number is automatically set to 10, and other values are ignored. The response is paginated at 100 per page if you have more than 100 mount targets.</p>"""
    marker: NotRequired["capo_efs.types.marker.Marker"]
    """<p>(Optional) Opaque pagination token returned from a previous <code>DescribeMountTargets</code> operation (String). If present, it specifies to continue the list from where the previous returning call left off.</p>"""
    file_system_id: NotRequired["capo_efs.types.file_system_id.FileSystemId"]
    """<p>(Optional) ID of the file system whose mount targets you want to list (String). It must be included in your request if an <code>AccessPointId</code> or <code>MountTargetId</code> is not included. Accepts either a file system ID or ARN as input.</p>"""
    mount_target_id: NotRequired["capo_efs.types.mount_target_id.MountTargetId"]
    """<p>(Optional) ID of the mount target that you want to have described (String). It must be included in your request if <code>FileSystemId</code> is not included. Accepts either a mount target ID or ARN as input.</p>"""
    access_point_id: NotRequired["capo_efs.types.access_point_id.AccessPointId"]
    """<p>(Optional) The ID of the access point whose mount targets that you want to list. It must be included in your request if a <code>FileSystemId</code> or <code>MountTargetId</code> is not included in your request. Accepts either an access point ID or ARN as input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMountTargetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeMountTargetsRequest:
    out: DescribeMountTargetsRequest = {}  # type: ignore[typeddict-item]
    return out
