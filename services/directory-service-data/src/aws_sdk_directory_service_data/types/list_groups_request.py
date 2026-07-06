"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#ListGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.max_results
    import aws_sdk_directory_service_data.types.next_token
    import aws_sdk_directory_service_data.types.realm


class ListGroupsRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    realm: NotRequired["aws_sdk_directory_service_data.types.realm.Realm"]
    """<p> The domain name associated with the directory. </p> <note> <p> This parameter is optional, so you can return groups outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive. </p> </note>"""
    next_token: NotRequired["aws_sdk_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""
    max_results: NotRequired[
        "aws_sdk_directory_service_data.types.max_results.MaxResults"
    ]
    """<p> The maximum number of results to be returned per request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsRequest) -> dict:
    out: dict = {}
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListGroupsRequest:
    out: ListGroupsRequest = {}  # type: ignore[typeddict-item]
    if "Realm" in data:
        out["realm"] = data["Realm"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
