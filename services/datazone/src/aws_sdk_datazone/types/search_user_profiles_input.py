"""Generated from Smithy shape ``com.amazonaws.datazone#SearchUserProfilesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.user_search_text
    import aws_sdk_datazone.types.user_search_type


class SearchUserProfilesInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which you want to search user profiles.</p>"""
    user_type: "aws_sdk_datazone.types.user_search_type.UserSearchType"
    """<p>Specifies the user type for the <code>SearchUserProfiles</code> action.</p>"""
    search_text: NotRequired["aws_sdk_datazone.types.user_search_text.UserSearchText"]
    """<p>Specifies the text for which to search.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call to <code>SearchUserProfiles</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchUserProfiles</code> to list the next set of results. </p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchUserProfiles</code> to list the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchUserProfilesInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.user_search_type

    out["userType"] = aws_sdk_datazone.types.user_search_type.serialize_json(
        value["user_type"]
    )
    if "search_text" in value:
        out["searchText"] = value["search_text"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchUserProfilesInput:
    out: SearchUserProfilesInput = {}  # type: ignore[typeddict-item]
    if "userType" in data:
        import aws_sdk_datazone.types.user_search_type

        out["user_type"] = aws_sdk_datazone.types.user_search_type.deserialize_json(
            data["userType"]
        )
    else:
        raise DeserializationError("SearchUserProfilesInput.user_type required")
    if "searchText" in data:
        out["search_text"] = data["searchText"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
