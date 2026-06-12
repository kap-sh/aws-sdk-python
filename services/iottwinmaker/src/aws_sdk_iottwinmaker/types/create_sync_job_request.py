"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateSyncJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.role_arn
    import aws_sdk_iottwinmaker.types.sync_source
    import aws_sdk_iottwinmaker.types.tag_map


class CreateSyncJobRequest(TypedDict):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The workspace ID.</p>"""
    sync_source: "aws_sdk_iottwinmaker.types.sync_source.SyncSource"
    """<p>The sync source.</p> <note> <p>Currently the only supported syncSoource is <code>SITEWISE </code>.</p> </note>"""
    sync_role: "aws_sdk_iottwinmaker.types.role_arn.RoleArn"
    """<p>The SyncJob IAM role. This IAM role is used by the SyncJob to read from the syncSource, and create, update, or delete the corresponding resources.</p>"""
    tags: NotRequired["aws_sdk_iottwinmaker.types.tag_map.TagMap"]
    """<p>The SyncJob tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSyncJobRequest) -> dict:
    out: dict = {}
    out["syncRole"] = value["sync_role"]
    if "tags" in value:
        import aws_sdk_iottwinmaker.types.tag_map

        out["tags"] = aws_sdk_iottwinmaker.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSyncJobRequest:
    out: CreateSyncJobRequest = {}  # type: ignore[typeddict-item]
    if "syncRole" in data:
        out["sync_role"] = data["syncRole"]
    else:
        raise DeserializationError("CreateSyncJobRequest.sync_role required")
    if "tags" in data:
        import aws_sdk_iottwinmaker.types.tag_map

        out["tags"] = aws_sdk_iottwinmaker.types.tag_map.deserialize_json(data["tags"])
    return out
