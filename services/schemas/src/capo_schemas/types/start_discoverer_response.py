"""Generated from Smithy shape ``com.amazonaws.schemas#StartDiscovererResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string
    import capo_schemas.types.discoverer_state


class StartDiscovererResponse(TypedDict, closed=True):
    discoverer_id: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The ID of the discoverer.</p>"""
    state: NotRequired["capo_schemas.types.discoverer_state.DiscovererState"]
    """<p>The state of the discoverer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDiscovererResponse) -> dict:
    out: dict = {}
    if "discoverer_id" in value:
        out["DiscovererId"] = value["discoverer_id"]
    if "state" in value:
        import capo_schemas.types.discoverer_state

        out["State"] = capo_schemas.types.discoverer_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> StartDiscovererResponse:
    out: StartDiscovererResponse = {}  # type: ignore[typeddict-item]
    if "DiscovererId" in data:
        out["discoverer_id"] = data["DiscovererId"]
    if "State" in data:
        import capo_schemas.types.discoverer_state

        out["state"] = capo_schemas.types.discoverer_state.deserialize_json(
            data["State"]
        )
    return out
