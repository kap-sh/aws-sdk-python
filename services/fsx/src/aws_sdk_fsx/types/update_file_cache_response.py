"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateFileCacheResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_cache


class UpdateFileCacheResponse(TypedDict):
    file_cache: NotRequired["aws_sdk_fsx.types.file_cache.FileCache"]
    """<p>A description of the cache that was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileCacheResponse) -> dict:
    out: dict = {}
    if "file_cache" in value:
        import aws_sdk_fsx.types.file_cache

        out["FileCache"] = aws_sdk_fsx.types.file_cache.serialize_aws_json_1_1(
            value["file_cache"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileCacheResponse:
    out: UpdateFileCacheResponse = {}  # type: ignore[typeddict-item]
    if "FileCache" in data:
        import aws_sdk_fsx.types.file_cache

        out["file_cache"] = aws_sdk_fsx.types.file_cache.deserialize_aws_json_1_1(
            data["FileCache"]
        )
    return out
