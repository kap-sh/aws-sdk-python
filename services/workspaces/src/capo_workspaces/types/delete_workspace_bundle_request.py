"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteWorkspaceBundleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.bundle_id


class DeleteWorkspaceBundleRequest(TypedDict, closed=True):
    bundle_id: NotRequired["capo_workspaces.types.bundle_id.BundleId"]
    """<p>The identifier of the bundle.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkspaceBundleRequest) -> dict:
    out: dict = {}
    if "bundle_id" in value:
        out["BundleId"] = value["bundle_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkspaceBundleRequest:
    out: DeleteWorkspaceBundleRequest = {}  # type: ignore[typeddict-item]
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    return out
