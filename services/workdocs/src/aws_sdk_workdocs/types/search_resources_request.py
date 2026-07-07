"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.additional_response_fields_list
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.filters
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.next_marker_type
    import aws_sdk_workdocs.types.search_query_scope_type_list
    import aws_sdk_workdocs.types.search_query_type
    import aws_sdk_workdocs.types.search_result_sort_list
    import aws_sdk_workdocs.types.search_results_limit_type


class SearchResourcesRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    query_text: NotRequired["aws_sdk_workdocs.types.search_query_type.SearchQueryType"]
    """<p>The String to search for. Searches across different text fields based on request parameters. Use double quotes around the query string for exact phrase matches.</p>"""
    query_scopes: NotRequired[
        "aws_sdk_workdocs.types.search_query_scope_type_list.SearchQueryScopeTypeList"
    ]
    """<p>Filter based on the text field type. A Folder has only a name and no content. A Comment has only content and no name. A Document or Document Version has a name and content</p>"""
    organization_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>Filters based on the resource owner OrgId. This is a mandatory parameter when using Admin SigV4 credentials.</p>"""
    additional_response_fields: NotRequired[
        "aws_sdk_workdocs.types.additional_response_fields_list.AdditionalResponseFieldsList"
    ]
    """<p>A list of attributes to include in the response. Used to request fields that are not normally returned in a standard response.</p>"""
    filters: NotRequired["aws_sdk_workdocs.types.filters.Filters"]
    """<p>Filters results based on entity metadata.</p>"""
    order_by: NotRequired[
        "aws_sdk_workdocs.types.search_result_sort_list.SearchResultSortList"
    ]
    """<p>Order by results in one or more categories.</p>"""
    limit: NotRequired[
        "aws_sdk_workdocs.types.search_results_limit_type.SearchResultsLimitType"
    ]
    """<p>Max results count per page.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.next_marker_type.NextMarkerType"]
    """<p>The marker for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesRequest) -> dict:
    out: dict = {}
    if "query_text" in value:
        out["QueryText"] = value["query_text"]
    if "query_scopes" in value:
        import aws_sdk_workdocs.types.search_query_scope_type_list

        out["QueryScopes"] = (
            aws_sdk_workdocs.types.search_query_scope_type_list.serialize_json(
                value["query_scopes"]
            )
        )
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    if "additional_response_fields" in value:
        import aws_sdk_workdocs.types.additional_response_fields_list

        out["AdditionalResponseFields"] = (
            aws_sdk_workdocs.types.additional_response_fields_list.serialize_json(
                value["additional_response_fields"]
            )
        )
    if "filters" in value:
        import aws_sdk_workdocs.types.filters

        out["Filters"] = aws_sdk_workdocs.types.filters.serialize_json(value["filters"])
    if "order_by" in value:
        import aws_sdk_workdocs.types.search_result_sort_list

        out["OrderBy"] = aws_sdk_workdocs.types.search_result_sort_list.serialize_json(
            value["order_by"]
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> SearchResourcesRequest:
    out: SearchResourcesRequest = {}  # type: ignore[typeddict-item]
    if "QueryText" in data:
        out["query_text"] = data["QueryText"]
    if "QueryScopes" in data:
        import aws_sdk_workdocs.types.search_query_scope_type_list

        out["query_scopes"] = (
            aws_sdk_workdocs.types.search_query_scope_type_list.deserialize_json(
                data["QueryScopes"]
            )
        )
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    if "AdditionalResponseFields" in data:
        import aws_sdk_workdocs.types.additional_response_fields_list

        out["additional_response_fields"] = (
            aws_sdk_workdocs.types.additional_response_fields_list.deserialize_json(
                data["AdditionalResponseFields"]
            )
        )
    if "Filters" in data:
        import aws_sdk_workdocs.types.filters

        out["filters"] = aws_sdk_workdocs.types.filters.deserialize_json(
            data["Filters"]
        )
    if "OrderBy" in data:
        import aws_sdk_workdocs.types.search_result_sort_list

        out["order_by"] = (
            aws_sdk_workdocs.types.search_result_sort_list.deserialize_json(
                data["OrderBy"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
