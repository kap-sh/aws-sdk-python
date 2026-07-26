"""Generated from Smithy shape ``com.amazonaws.iot#ListAuthorizersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.authorizers
    import capo_iot.types.marker


class ListAuthorizersResponse(TypedDict, closed=True):
    authorizers: NotRequired["capo_iot.types.authorizers.Authorizers"]
    """<p>The authorizers.</p>"""
    next_marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>A marker used to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuthorizersResponse) -> dict:
    out: dict = {}
    if "authorizers" in value:
        import capo_iot.types.authorizers

        out["authorizers"] = capo_iot.types.authorizers.serialize_json(
            value["authorizers"]
        )
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListAuthorizersResponse:
    out: ListAuthorizersResponse = {}  # type: ignore[typeddict-item]
    if "authorizers" in data:
        import capo_iot.types.authorizers

        out["authorizers"] = capo_iot.types.authorizers.deserialize_json(
            data["authorizers"]
        )
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
