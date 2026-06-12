"""Generated from Smithy shape ``com.amazonaws.entityresolution#BatchDeleteUniqueIdInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.unique_id_list

class BatchDeleteUniqueIdInput(TypedDict):
    workflow_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""
    input_source: NotRequired["str"]
    """<p>The input source for the batch delete unique ID operation.</p>"""
    unique_ids: "aws_sdk_entityresolution.types.unique_id_list.UniqueIdList"
    """<p>The unique IDs to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteUniqueIdInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BatchDeleteUniqueIdInput:
    out: BatchDeleteUniqueIdInput = {}  # type: ignore[typeddict-item]
    return out