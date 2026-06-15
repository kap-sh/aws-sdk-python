"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#SearchGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.ldap_display_name_list
    import aws_sdk_directory_service_data.types.max_results
    import aws_sdk_directory_service_data.types.next_token
    import aws_sdk_directory_service_data.types.realm
    import aws_sdk_directory_service_data.types.search_string


class SearchGroupsRequest(TypedDict):
    directory_id: "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    search_string: "aws_sdk_directory_service_data.types.search_string.SearchString"
    r"""<p> The attribute value that you want to search for. </p> <note> <p> Wildcard <code>(*)</code> searches aren't supported. For a list of supported attributes, see <a href=\"https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html\">Directory Service Data Attributes</a>. </p> </note>"""
    search_attributes: "aws_sdk_directory_service_data.types.ldap_display_name_list.LdapDisplayNameList"
    r"""<p> One or more data attributes that are used to search for a group. For a list of supported attributes, see <a href=\"https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html\">Directory Service Data Attributes</a>. </p>"""
    realm: NotRequired["aws_sdk_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group. </p> <note> <p> This parameter is optional, so you can return groups outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive. </p> </note>"""
    next_token: NotRequired["aws_sdk_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""
    max_results: NotRequired[
        "aws_sdk_directory_service_data.types.max_results.MaxResults"
    ]
    """<p> The maximum number of results to be returned per request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchGroupsRequest) -> dict:
    out: dict = {}
    out["SearchString"] = value["search_string"]
    import aws_sdk_directory_service_data.types.ldap_display_name_list

    out["SearchAttributes"] = (
        aws_sdk_directory_service_data.types.ldap_display_name_list.serialize_json(
            value["search_attributes"]
        )
    )
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> SearchGroupsRequest:
    out: SearchGroupsRequest = {}  # type: ignore[typeddict-item]
    if "SearchString" in data:
        out["search_string"] = data["SearchString"]
    else:
        raise DeserializationError("SearchGroupsRequest.search_string required")
    if "SearchAttributes" in data:
        import aws_sdk_directory_service_data.types.ldap_display_name_list

        out["search_attributes"] = (
            aws_sdk_directory_service_data.types.ldap_display_name_list.deserialize_json(
                data["SearchAttributes"]
            )
        )
    else:
        raise DeserializationError("SearchGroupsRequest.search_attributes required")
    if "Realm" in data:
        out["realm"] = data["Realm"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
