"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeDirectoriesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_descriptions
    import aws_sdk_directory_service.types.next_token


class DescribeDirectoriesResult(TypedDict):
    directory_descriptions: NotRequired[
        "aws_sdk_directory_service.types.directory_descriptions.DirectoryDescriptions"
    ]
    """<p>The list of available <a>DirectoryDescription</a> objects that were retrieved.</p> <p>It is possible that this list contains less than the number of items specified in the <code>Limit</code> member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.</p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>If not null, more results are available. Pass this value for the <code>NextToken</code> parameter in a subsequent call to <a>DescribeDirectories</a> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDirectoriesResult) -> dict:
    out: dict = {}
    if "directory_descriptions" in value:
        import aws_sdk_directory_service.types.directory_descriptions

        out["DirectoryDescriptions"] = (
            aws_sdk_directory_service.types.directory_descriptions.serialize_aws_json_1_1(
                value["directory_descriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDirectoriesResult:
    out: DescribeDirectoriesResult = {}  # type: ignore[typeddict-item]
    if "DirectoryDescriptions" in data:
        import aws_sdk_directory_service.types.directory_descriptions

        out["directory_descriptions"] = (
            aws_sdk_directory_service.types.directory_descriptions.deserialize_aws_json_1_1(
                data["DirectoryDescriptions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
