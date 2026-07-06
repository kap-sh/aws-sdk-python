"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetSyncJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.sync_source


class GetSyncJobRequest(TypedDict, closed=True):
    sync_source: "aws_sdk_iottwinmaker.types.sync_source.SyncSource"
    """<p>The sync source.</p> <note> <p>Currently the only supported syncSource is <code>SITEWISE </code>.</p> </note>"""
    workspace_id: NotRequired["aws_sdk_iottwinmaker.types.id.Id"]
    """<p>The workspace ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSyncJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSyncJobRequest:
    out: GetSyncJobRequest = {}  # type: ignore[typeddict-item]
    return out
