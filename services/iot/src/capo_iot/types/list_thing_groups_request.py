"""Generated from Smithy shape ``com.amazonaws.iot#ListThingGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.recursive_without_default
    import capo_iot.types.registry_max_results
    import capo_iot.types.thing_group_name


class ListThingGroupsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired["capo_iot.types.registry_max_results.RegistryMaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""
    parent_group: NotRequired["capo_iot.types.thing_group_name.ThingGroupName"]
    """<p>A filter that limits the results to those with the specified parent group.</p>"""
    name_prefix_filter: NotRequired["capo_iot.types.thing_group_name.ThingGroupName"]
    """<p>A filter that limits the results to those with the specified name prefix.</p>"""
    recursive: NotRequired[
        "capo_iot.types.recursive_without_default.RecursiveWithoutDefault"
    ]
    """<p>If true, return child groups as well.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThingGroupsRequest:
    out: ListThingGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
