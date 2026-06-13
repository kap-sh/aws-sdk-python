"""Generated from Smithy shape ``com.amazonaws.omics#DeleteRunCacheRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_cache_id


class DeleteRunCacheRequest(TypedDict):
    id: "aws_sdk_omics.types.run_cache_id.RunCacheId"
    """<p>Run cache identifier for the cache you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRunCacheRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRunCacheRequest:
    out: DeleteRunCacheRequest = {}  # type: ignore[typeddict-item]
    return out
