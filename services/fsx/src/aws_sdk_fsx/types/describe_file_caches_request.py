"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeFileCachesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_cache_ids
    import aws_sdk_fsx.types.max_results
    import aws_sdk_fsx.types.next_token


class DescribeFileCachesRequest(TypedDict):
    file_cache_ids: NotRequired["aws_sdk_fsx.types.file_cache_ids.FileCacheIds"]
    """<p>IDs of the caches whose descriptions you want to retrieve (String).</p>"""
    max_results: NotRequired["aws_sdk_fsx.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileCachesRequest) -> dict:
    out: dict = {}
    if "file_cache_ids" in value:
        import aws_sdk_fsx.types.file_cache_ids

        out["FileCacheIds"] = aws_sdk_fsx.types.file_cache_ids.serialize_aws_json_1_1(
            value["file_cache_ids"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileCachesRequest:
    out: DescribeFileCachesRequest = {}  # type: ignore[typeddict-item]
    if "FileCacheIds" in data:
        import aws_sdk_fsx.types.file_cache_ids

        out["file_cache_ids"] = (
            aws_sdk_fsx.types.file_cache_ids.deserialize_aws_json_1_1(
                data["FileCacheIds"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
