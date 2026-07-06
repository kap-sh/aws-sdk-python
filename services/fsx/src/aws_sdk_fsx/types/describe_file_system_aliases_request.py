"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeFileSystemAliasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.file_system_id
    import aws_sdk_fsx.types.max_results
    import aws_sdk_fsx.types.next_token


class DescribeFileSystemAliasesRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    file_system_id: NotRequired["aws_sdk_fsx.types.file_system_id.FileSystemId"]
    """<p>The ID of the file system to return the associated DNS aliases for (String).</p>"""
    max_results: NotRequired["aws_sdk_fsx.types.max_results.MaxResults"]
    """<p>Maximum number of DNS aliases to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the <code>MaxResults</code> parameter specified in the request and the service's internal maximum number of items per page.</p>"""
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]
    """<p>Opaque pagination token returned from a previous <code>DescribeFileSystemAliases</code> operation (String). If a token is included in the request, the action continues the list from where the previous returning call left off.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileSystemAliasesRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileSystemAliasesRequest:
    out: DescribeFileSystemAliasesRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
