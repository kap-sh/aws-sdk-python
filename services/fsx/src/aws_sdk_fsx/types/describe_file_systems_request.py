"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeFileSystemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_system_ids
    import aws_sdk_fsx.types.max_results
    import aws_sdk_fsx.types.next_token


class DescribeFileSystemsRequest(TypedDict, closed=True):
    file_system_ids: NotRequired["aws_sdk_fsx.types.file_system_ids.FileSystemIds"]
    """<p>IDs of the file systems whose descriptions you want to retrieve (String).</p>"""
    max_results: NotRequired["aws_sdk_fsx.types.max_results.MaxResults"]
    """<p>Maximum number of file systems to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the <code>MaxResults</code> parameter specified in the request and the service's internal maximum number of items per page.</p>"""
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]
    """<p>Opaque pagination token returned from a previous <code>DescribeFileSystems</code> operation (String). If a token present, the operation continues the list from where the returning call left off.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileSystemsRequest) -> dict:
    out: dict = {}
    if "file_system_ids" in value:
        import aws_sdk_fsx.types.file_system_ids

        out["FileSystemIds"] = aws_sdk_fsx.types.file_system_ids.serialize_aws_json_1_1(
            value["file_system_ids"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileSystemsRequest:
    out: DescribeFileSystemsRequest = {}  # type: ignore[typeddict-item]
    if "FileSystemIds" in data:
        import aws_sdk_fsx.types.file_system_ids

        out["file_system_ids"] = (
            aws_sdk_fsx.types.file_system_ids.deserialize_aws_json_1_1(
                data["FileSystemIds"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
