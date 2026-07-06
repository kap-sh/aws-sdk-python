"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeSharedDirectoriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.directory_ids
    import aws_sdk_directory_service.types.limit
    import aws_sdk_directory_service.types.next_token


class DescribeSharedDirectoriesRequest(TypedDict, closed=True):
    owner_directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>Returns the identifier of the directory in the directory owner account. </p>"""
    shared_directory_ids: NotRequired[
        "aws_sdk_directory_service.types.directory_ids.DirectoryIds"
    ]
    """<p>A list of identifiers of all shared directories in your account. </p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>The <code>DescribeSharedDirectoriesResult.NextToken</code> value from a previous call to <a>DescribeSharedDirectories</a>. Pass null if this is the first call. </p>"""
    limit: NotRequired["aws_sdk_directory_service.types.limit.Limit"]
    """<p>The number of shared directories to return in the response object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSharedDirectoriesRequest) -> dict:
    out: dict = {}
    out["OwnerDirectoryId"] = value["owner_directory_id"]
    if "shared_directory_ids" in value:
        import aws_sdk_directory_service.types.directory_ids

        out["SharedDirectoryIds"] = (
            aws_sdk_directory_service.types.directory_ids.serialize_aws_json_1_1(
                value["shared_directory_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSharedDirectoriesRequest:
    out: DescribeSharedDirectoriesRequest = {}  # type: ignore[typeddict-item]
    if "OwnerDirectoryId" in data:
        out["owner_directory_id"] = data["OwnerDirectoryId"]
    else:
        raise DeserializationError(
            "DescribeSharedDirectoriesRequest.owner_directory_id required"
        )
    if "SharedDirectoryIds" in data:
        import aws_sdk_directory_service.types.directory_ids

        out["shared_directory_ids"] = (
            aws_sdk_directory_service.types.directory_ids.deserialize_aws_json_1_1(
                data["SharedDirectoryIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
