"""Generated from Smithy shape ``com.amazonaws.omics#StartRunBatchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.batch_arn
    import capo_omics.types.batch_id
    import capo_omics.types.batch_status
    import capo_omics.types.batch_uuid
    import capo_omics.types.tag_map


class StartRunBatchResponse(TypedDict, closed=True):
    id: NotRequired["capo_omics.types.batch_id.BatchId"]
    """<p>The identifier portion of the run batch ARN.</p>"""
    arn: NotRequired["capo_omics.types.batch_arn.BatchArn"]
    """<p>The unique ARN of the run batch.</p>"""
    status: NotRequired["capo_omics.types.batch_status.BatchStatus"]
    """<p>The initial status of the run batch. Returns <code>CREATING</code> while the batch is being initialized.</p>"""
    uuid: NotRequired["capo_omics.types.batch_uuid.BatchUuid"]
    """<p>The universally unique identifier (UUID) for the run batch.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>AWS tags associated with the run batch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRunBatchResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartRunBatchResponse:
    out: StartRunBatchResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        out["status"] = data["status"]
    if "uuid" in data:
        out["uuid"] = data["uuid"]
    if "tags" in data:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    return out
