"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListIncidentRecordsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.filter_list
    import capo_ssm_incidents.types.max_results
    import capo_ssm_incidents.types.next_token


class ListIncidentRecordsInput(TypedDict, closed=True):
    filters: NotRequired["capo_ssm_incidents.types.filter_list.FilterList"]
    """<p>Filters the list of incident records you want to search through. You can filter on the following keys:</p> <ul> <li> <p> <code>creationTime</code> </p> </li> <li> <p> <code>impact</code> </p> </li> <li> <p> <code>status</code> </p> </li> <li> <p> <code>createdBy</code> </p> </li> </ul> <p>Note the following when when you use Filters:</p> <ul> <li> <p>If you don't specify a Filter, the response includes all incident records.</p> </li> <li> <p>If you specify more than one filter in a single request, the response returns incident records that match all filters.</p> </li> <li> <p>If you specify a filter with more than one value, the response returns incident records that match any of the values provided.</p> </li> </ul>"""
    max_results: NotRequired["capo_ssm_incidents.types.max_results.MaxResults"]
    """<p>The maximum number of results per page.</p>"""
    next_token: NotRequired["capo_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIncidentRecordsInput) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_ssm_incidents.types.filter_list

        out["filters"] = capo_ssm_incidents.types.filter_list.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIncidentRecordsInput:
    out: ListIncidentRecordsInput = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_ssm_incidents.types.filter_list

        out["filters"] = capo_ssm_incidents.types.filter_list.deserialize_json(
            data["filters"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
