"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteFileCacheResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_cache_id
    import aws_sdk_fsx.types.file_cache_lifecycle


class DeleteFileCacheResponse(TypedDict, closed=True):
    file_cache_id: NotRequired["aws_sdk_fsx.types.file_cache_id.FileCacheId"]
    """<p>The ID of the cache that's being deleted.</p>"""
    lifecycle: NotRequired["aws_sdk_fsx.types.file_cache_lifecycle.FileCacheLifecycle"]
    """<p>The cache lifecycle for the deletion request. If the <code>DeleteFileCache</code> operation is successful, this status is <code>DELETING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileCacheResponse) -> dict:
    out: dict = {}
    if "file_cache_id" in value:
        out["FileCacheId"] = value["file_cache_id"]
    if "lifecycle" in value:
        import aws_sdk_fsx.types.file_cache_lifecycle

        out["Lifecycle"] = (
            aws_sdk_fsx.types.file_cache_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileCacheResponse:
    out: DeleteFileCacheResponse = {}  # type: ignore[typeddict-item]
    if "FileCacheId" in data:
        out["file_cache_id"] = data["FileCacheId"]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.file_cache_lifecycle

        out["lifecycle"] = (
            aws_sdk_fsx.types.file_cache_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    return out
