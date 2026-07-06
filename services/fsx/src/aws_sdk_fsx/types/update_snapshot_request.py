"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.snapshot_id
    import aws_sdk_fsx.types.snapshot_name


class UpdateSnapshotRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    name: NotRequired["aws_sdk_fsx.types.snapshot_name.SnapshotName"]
    """<p>The name of the snapshot to update.</p>"""
    snapshot_id: NotRequired["aws_sdk_fsx.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot that you want to update, in the format <code>fsvolsnap-0123456789abcdef0</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSnapshotRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "name" in value:
        out["Name"] = value["name"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSnapshotRequest:
    out: UpdateSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    return out
