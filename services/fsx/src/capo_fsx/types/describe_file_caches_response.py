"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeFileCachesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.file_caches
    import capo_fsx.types.next_token


class DescribeFileCachesResponse(TypedDict, closed=True):
    file_caches: NotRequired["capo_fsx.types.file_caches.FileCaches"]
    """<p>The response object for the <code>DescribeFileCaches</code> operation.</p>"""
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileCachesResponse) -> dict:
    out: dict = {}
    if "file_caches" in value:
        import capo_fsx.types.file_caches

        out["FileCaches"] = capo_fsx.types.file_caches.serialize_aws_json_1_1(
            value["file_caches"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileCachesResponse:
    out: DescribeFileCachesResponse = {}  # type: ignore[typeddict-item]
    if "FileCaches" in data:
        import capo_fsx.types.file_caches

        out["file_caches"] = capo_fsx.types.file_caches.deserialize_aws_json_1_1(
            data["FileCaches"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
