"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeSharedDirectoriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.next_token
    import aws_sdk_directory_service.types.shared_directories


class DescribeSharedDirectoriesResult(TypedDict, closed=True):
    shared_directories: NotRequired[
        "aws_sdk_directory_service.types.shared_directories.SharedDirectories"
    ]
    """<p>A list of all shared directories in your account.</p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>If not null, token that indicates that more results are available. Pass this value for the <code>NextToken</code> parameter in a subsequent call to <a>DescribeSharedDirectories</a> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSharedDirectoriesResult) -> dict:
    out: dict = {}
    if "shared_directories" in value:
        import aws_sdk_directory_service.types.shared_directories

        out["SharedDirectories"] = (
            aws_sdk_directory_service.types.shared_directories.serialize_aws_json_1_1(
                value["shared_directories"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSharedDirectoriesResult:
    out: DescribeSharedDirectoriesResult = {}  # type: ignore[typeddict-item]
    if "SharedDirectories" in data:
        import aws_sdk_directory_service.types.shared_directories

        out["shared_directories"] = (
            aws_sdk_directory_service.types.shared_directories.deserialize_aws_json_1_1(
                data["SharedDirectories"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
