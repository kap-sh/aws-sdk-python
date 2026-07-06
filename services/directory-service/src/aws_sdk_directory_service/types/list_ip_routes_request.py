"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListIpRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.limit
    import aws_sdk_directory_service.types.next_token


class ListIpRoutesRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier (ID) of the directory for which you want to retrieve the IP addresses.</p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>The <i>ListIpRoutes.NextToken</i> value from a previous call to <a>ListIpRoutes</a>. Pass null if this is the first call.</p>"""
    limit: NotRequired["aws_sdk_directory_service.types.limit.Limit"]
    """<p>Maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIpRoutesRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIpRoutesRequest:
    out: ListIpRoutesRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("ListIpRoutesRequest.directory_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
