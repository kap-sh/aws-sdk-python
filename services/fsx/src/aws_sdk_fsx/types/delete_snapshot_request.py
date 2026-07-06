"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.snapshot_id


class DeleteSnapshotRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    snapshot_id: NotRequired["aws_sdk_fsx.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotRequest:
    out: DeleteSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    return out
