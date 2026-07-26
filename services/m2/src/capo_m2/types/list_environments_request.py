"""Generated from Smithy shape ``com.amazonaws.m2#ListEnvironmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.engine_type
    import capo_m2.types.entity_name_list
    import capo_m2.types.max_results
    import capo_m2.types.next_token


class ListEnvironmentsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>A pagination token to control the number of runtime environments displayed in the list.</p>"""
    max_results: NotRequired["capo_m2.types.max_results.MaxResults"]
    """<p>The maximum number of runtime environments to return.</p>"""
    names: NotRequired["capo_m2.types.entity_name_list.EntityNameList"]
    """<p>The names of the runtime environments. Must be unique within the account.</p>"""
    engine_type: NotRequired["capo_m2.types.engine_type.EngineType"]
    """<p>The engine type for the runtime environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnvironmentsRequest:
    out: ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    return out
