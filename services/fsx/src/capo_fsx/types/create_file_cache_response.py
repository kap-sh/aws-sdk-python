"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileCacheResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.file_cache_creating


class CreateFileCacheResponse(TypedDict, closed=True):
    file_cache: NotRequired["capo_fsx.types.file_cache_creating.FileCacheCreating"]
    """<p>A description of the cache that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFileCacheResponse) -> dict:
    out: dict = {}
    if "file_cache" in value:
        import capo_fsx.types.file_cache_creating

        out["FileCache"] = capo_fsx.types.file_cache_creating.serialize_aws_json_1_1(
            value["file_cache"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFileCacheResponse:
    out: CreateFileCacheResponse = {}  # type: ignore[typeddict-item]
    if "FileCache" in data:
        import capo_fsx.types.file_cache_creating

        out["file_cache"] = capo_fsx.types.file_cache_creating.deserialize_aws_json_1_1(
            data["FileCache"]
        )
    return out
