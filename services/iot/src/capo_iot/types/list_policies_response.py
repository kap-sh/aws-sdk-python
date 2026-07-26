"""Generated from Smithy shape ``com.amazonaws.iot#ListPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.marker
    import capo_iot.types.policies


class ListPoliciesResponse(TypedDict, closed=True):
    policies: NotRequired["capo_iot.types.policies.Policies"]
    """<p>The descriptions of the policies.</p>"""
    next_marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>The marker for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPoliciesResponse) -> dict:
    out: dict = {}
    if "policies" in value:
        import capo_iot.types.policies

        out["policies"] = capo_iot.types.policies.serialize_json(value["policies"])
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListPoliciesResponse:
    out: ListPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "policies" in data:
        import capo_iot.types.policies

        out["policies"] = capo_iot.types.policies.deserialize_json(data["policies"])
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
