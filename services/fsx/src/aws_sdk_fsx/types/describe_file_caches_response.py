"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeFileCachesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_caches
    import aws_sdk_fsx.types.next_token


class DescribeFileCachesResponse(TypedDict):
    file_caches: NotRequired["aws_sdk_fsx.types.file_caches.FileCaches"]
    """<p>The response object for the <code>DescribeFileCaches</code> operation.</p>"""
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileCachesResponse) -> dict:
    out: dict = {}
    if "file_caches" in value:
        import aws_sdk_fsx.types.file_caches

        out["FileCaches"] = aws_sdk_fsx.types.file_caches.serialize_aws_json_1_1(
            value["file_caches"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileCachesResponse:
    out: DescribeFileCachesResponse = {}  # type: ignore[typeddict-item]
    if "FileCaches" in data:
        import aws_sdk_fsx.types.file_caches

        out["file_caches"] = aws_sdk_fsx.types.file_caches.deserialize_aws_json_1_1(
            data["FileCaches"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
