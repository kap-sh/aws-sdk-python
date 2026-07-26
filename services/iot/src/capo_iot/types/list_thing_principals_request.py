"""Generated from Smithy shape ``com.amazonaws.iot#ListThingPrincipalsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.registry_max_results
    import capo_iot.types.thing_name


class ListThingPrincipalsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired["capo_iot.types.registry_max_results.RegistryMaxResults"]
    """<p>The maximum number of results to return in this operation.</p>"""
    thing_name: "capo_iot.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingPrincipalsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThingPrincipalsRequest:
    out: ListThingPrincipalsRequest = {}  # type: ignore[typeddict-item]
    return out
