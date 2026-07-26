"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.condition_list
    import capo_resiliencehub.types.field_list
    import capo_resiliencehub.types.max_results
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.sort_list
    import capo_resiliencehub.types.string255


class ListMetricsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Null, or the token from a previous call to get the next set of results.</p>"""
    max_results: NotRequired["capo_resiliencehub.types.max_results.MaxResults"]
    """<p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    fields: NotRequired["capo_resiliencehub.types.field_list.FieldList"]
    """<p>Indicates the list of fields in the data source.</p>"""
    data_source: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>Indicates the data source of the metrics.</p>"""
    conditions: NotRequired["capo_resiliencehub.types.condition_list.ConditionList"]
    """<p>Indicates the list of all the conditions that were applied on the metrics.</p>"""
    sorts: NotRequired["capo_resiliencehub.types.sort_list.SortList"]
    """<p>(Optional) Indicates the order in which you want to sort the fields in the metrics. By default, the fields are sorted in the ascending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMetricsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "fields" in value:
        import capo_resiliencehub.types.field_list

        out["fields"] = capo_resiliencehub.types.field_list.serialize_json(
            value["fields"]
        )
    if "data_source" in value:
        out["dataSource"] = value["data_source"]
    if "conditions" in value:
        import capo_resiliencehub.types.condition_list

        out["conditions"] = capo_resiliencehub.types.condition_list.serialize_json(
            value["conditions"]
        )
    if "sorts" in value:
        import capo_resiliencehub.types.sort_list

        out["sorts"] = capo_resiliencehub.types.sort_list.serialize_json(value["sorts"])
    return out


def deserialize_json(data: dict) -> ListMetricsRequest:
    out: ListMetricsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "fields" in data:
        import capo_resiliencehub.types.field_list

        out["fields"] = capo_resiliencehub.types.field_list.deserialize_json(
            data["fields"]
        )
    if "dataSource" in data:
        out["data_source"] = data["dataSource"]
    if "conditions" in data:
        import capo_resiliencehub.types.condition_list

        out["conditions"] = capo_resiliencehub.types.condition_list.deserialize_json(
            data["conditions"]
        )
    if "sorts" in data:
        import capo_resiliencehub.types.sort_list

        out["sorts"] = capo_resiliencehub.types.sort_list.deserialize_json(
            data["sorts"]
        )
    return out
