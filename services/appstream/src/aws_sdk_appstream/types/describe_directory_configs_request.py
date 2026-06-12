"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeDirectoryConfigsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.directory_name_list
    import aws_sdk_appstream.types.integer
    import aws_sdk_appstream.types.string


class DescribeDirectoryConfigsRequest(TypedDict):
    directory_names: NotRequired[
        "aws_sdk_appstream.types.directory_name_list.DirectoryNameList"
    ]
    """<p>The directory names.</p>"""
    max_results: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDirectoryConfigsRequest) -> dict:
    out: dict = {}
    if "directory_names" in value:
        import aws_sdk_appstream.types.directory_name_list

        out["DirectoryNames"] = (
            aws_sdk_appstream.types.directory_name_list.serialize_aws_json_1_1(
                value["directory_names"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDirectoryConfigsRequest:
    out: DescribeDirectoryConfigsRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryNames" in data:
        import aws_sdk_appstream.types.directory_name_list

        out["directory_names"] = (
            aws_sdk_appstream.types.directory_name_list.deserialize_aws_json_1_1(
                data["DirectoryNames"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
