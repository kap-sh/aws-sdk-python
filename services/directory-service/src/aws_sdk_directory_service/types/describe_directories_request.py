"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeDirectoriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_ids
    import aws_sdk_directory_service.types.limit
    import aws_sdk_directory_service.types.next_token


class DescribeDirectoriesRequest(TypedDict, closed=True):
    directory_ids: NotRequired[
        "aws_sdk_directory_service.types.directory_ids.DirectoryIds"
    ]
    """<p>A list of identifiers of the directories for which to obtain the information. If this member is null, all directories that belong to the current account are returned.</p> <p>An empty list results in an <code>InvalidParameterException</code> being thrown.</p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>The <code>DescribeDirectoriesResult.NextToken</code> value from a previous call to <a>DescribeDirectories</a>. Pass null if this is the first call.</p>"""
    limit: NotRequired["aws_sdk_directory_service.types.limit.Limit"]
    """<p>The maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDirectoriesRequest) -> dict:
    out: dict = {}
    if "directory_ids" in value:
        import aws_sdk_directory_service.types.directory_ids

        out["DirectoryIds"] = (
            aws_sdk_directory_service.types.directory_ids.serialize_aws_json_1_1(
                value["directory_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDirectoriesRequest:
    out: DescribeDirectoriesRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryIds" in data:
        import aws_sdk_directory_service.types.directory_ids

        out["directory_ids"] = (
            aws_sdk_directory_service.types.directory_ids.deserialize_aws_json_1_1(
                data["DirectoryIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
