"""Generated from Smithy shape ``com.amazonaws.fsx#CreateSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.snapshot_name
    import aws_sdk_fsx.types.tags
    import aws_sdk_fsx.types.volume_id


class CreateSnapshotRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    name: NotRequired["aws_sdk_fsx.types.snapshot_name.SnapshotName"]
    """<p>The name of the snapshot. </p>"""
    volume_id: NotRequired["aws_sdk_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the volume that you are taking a snapshot of.</p>"""
    tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "name" in value:
        out["Name"] = value["name"]
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "tags" in value:
        import aws_sdk_fsx.types.tags

        out["Tags"] = aws_sdk_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotRequest:
    out: CreateSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "Tags" in data:
        import aws_sdk_fsx.types.tags

        out["tags"] = aws_sdk_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
