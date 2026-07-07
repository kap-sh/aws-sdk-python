"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DeleteSyncJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.sync_source


class DeleteSyncJobRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The workspace ID.</p>"""
    sync_source: "aws_sdk_iottwinmaker.types.sync_source.SyncSource"
    """<p>The sync source.</p> <note> <p>Currently the only supported syncSource is <code>SITEWISE </code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSyncJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSyncJobRequest:
    out: DeleteSyncJobRequest = {}  # type: ignore[typeddict-item]
    return out
