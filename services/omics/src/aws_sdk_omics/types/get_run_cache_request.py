"""Generated from Smithy shape ``com.amazonaws.omics#GetRunCacheRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_cache_id


class GetRunCacheRequest(TypedDict):
    id: "aws_sdk_omics.types.run_cache_id.RunCacheId"
    """<p>The identifier of the run cache to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRunCacheRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRunCacheRequest:
    out: GetRunCacheRequest = {}  # type: ignore[typeddict-item]
    return out
