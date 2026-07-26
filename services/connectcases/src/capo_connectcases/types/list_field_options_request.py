"""Generated from Smithy shape ``com.amazonaws.connectcases#ListFieldOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_id
    import capo_connectcases.types.max_results
    import capo_connectcases.types.next_token
    import capo_connectcases.types.values_list


class ListFieldOptionsRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    field_id: "capo_connectcases.types.field_id.FieldId"
    """<p>The unique identifier of a field.</p>"""
    max_results: NotRequired["capo_connectcases.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    values: NotRequired["capo_connectcases.types.values_list.ValuesList"]
    """<p>A list of <code>FieldOption</code> values to filter on for <code>ListFieldOptions</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFieldOptionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFieldOptionsRequest:
    out: ListFieldOptionsRequest = {}  # type: ignore[typeddict-item]
    return out
