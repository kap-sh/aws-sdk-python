"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchCasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_filter
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_identifier_list
    import capo_connectcases.types.next_token
    import capo_connectcases.types.sort_list


class SearchCasesRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of cases to return. When no value is provided, 25 is the default.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    search_term: NotRequired["str"]
    """<p>A word or phrase used to perform a quick search.</p>"""
    filter: NotRequired["capo_connectcases.types.case_filter.CaseFilter"]
    """<p>A list of filter objects.</p>"""
    sorts: NotRequired["capo_connectcases.types.sort_list.SortList"]
    """<p>A list of sorts where each sort specifies a field and their sort order to be applied to the results. </p>"""
    fields: NotRequired[
        "capo_connectcases.types.field_identifier_list.FieldIdentifierList"
    ]
    """<p>The list of field identifiers to be returned as part of the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchCasesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "search_term" in value:
        out["searchTerm"] = value["search_term"]
    if "filter" in value:
        import capo_connectcases.types.case_filter

        out["filter"] = capo_connectcases.types.case_filter.serialize_json(
            value["filter"]
        )
    if "sorts" in value:
        import capo_connectcases.types.sort_list

        out["sorts"] = capo_connectcases.types.sort_list.serialize_json(value["sorts"])
    if "fields" in value:
        import capo_connectcases.types.field_identifier_list

        out["fields"] = capo_connectcases.types.field_identifier_list.serialize_json(
            value["fields"]
        )
    return out


def deserialize_json(data: dict) -> SearchCasesRequest:
    out: SearchCasesRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "searchTerm" in data:
        out["search_term"] = data["searchTerm"]
    if "filter" in data:
        import capo_connectcases.types.case_filter

        out["filter"] = capo_connectcases.types.case_filter.deserialize_json(
            data["filter"]
        )
    if "sorts" in data:
        import capo_connectcases.types.sort_list

        out["sorts"] = capo_connectcases.types.sort_list.deserialize_json(data["sorts"])
    if "fields" in data:
        import capo_connectcases.types.field_identifier_list

        out["fields"] = capo_connectcases.types.field_identifier_list.deserialize_json(
            data["fields"]
        )
    return out
