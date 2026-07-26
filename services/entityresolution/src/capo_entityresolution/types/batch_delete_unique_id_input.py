"""Generated from Smithy shape ``com.amazonaws.entityresolution#BatchDeleteUniqueIdInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.unique_id_list


class BatchDeleteUniqueIdInput(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""
    input_source: NotRequired["str"]
    """<p>The input source for the batch delete unique ID operation.</p>"""
    unique_ids: "capo_entityresolution.types.unique_id_list.UniqueIdList"
    """<p>The unique IDs to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteUniqueIdInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BatchDeleteUniqueIdInput:
    out: BatchDeleteUniqueIdInput = {}  # type: ignore[typeddict-item]
    return out
