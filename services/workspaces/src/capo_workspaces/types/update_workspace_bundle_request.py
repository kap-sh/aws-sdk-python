"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateWorkspaceBundleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.bundle_id
    import capo_workspaces.types.workspace_image_id


class UpdateWorkspaceBundleRequest(TypedDict, closed=True):
    bundle_id: NotRequired["capo_workspaces.types.bundle_id.BundleId"]
    """<p>The identifier of the bundle.</p>"""
    image_id: NotRequired["capo_workspaces.types.workspace_image_id.WorkspaceImageId"]
    """<p>The identifier of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkspaceBundleRequest) -> dict:
    out: dict = {}
    if "bundle_id" in value:
        out["BundleId"] = value["bundle_id"]
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkspaceBundleRequest:
    out: UpdateWorkspaceBundleRequest = {}  # type: ignore[typeddict-item]
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    return out
