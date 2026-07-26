"""Generated from Smithy shape ``com.amazonaws.omics#CreateRunCacheResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.run_cache_arn
    import capo_omics.types.run_cache_id
    import capo_omics.types.run_cache_status
    import capo_omics.types.tag_map


class CreateRunCacheResponse(TypedDict, closed=True):
    arn: NotRequired["capo_omics.types.run_cache_arn.RunCacheArn"]
    """<p>Unique resource identifier for the run cache.</p>"""
    id: NotRequired["capo_omics.types.run_cache_id.RunCacheId"]
    """<p>Identifier for the run cache.</p>"""
    status: NotRequired["capo_omics.types.run_cache_status.RunCacheStatus"]
    """<p>Run cache status.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>The tags associated with this run cache.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRunCacheResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRunCacheResponse:
    out: CreateRunCacheResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "tags" in data:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    return out
