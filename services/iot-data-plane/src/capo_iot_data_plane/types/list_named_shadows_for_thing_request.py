"""Generated from Smithy shape ``com.amazonaws.iotdataplane#ListNamedShadowsForThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.next_token
    import capo_iot_data_plane.types.page_size
    import capo_iot_data_plane.types.thing_name


class ListNamedShadowsForThingRequest(TypedDict, closed=True):
    thing_name: "capo_iot_data_plane.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""
    next_token: NotRequired["capo_iot_data_plane.types.next_token.NextToken"]
    """<p>The token to retrieve the next set of results.</p>"""
    page_size: NotRequired["capo_iot_data_plane.types.page_size.PageSize"]
    """<p>The result page size.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNamedShadowsForThingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNamedShadowsForThingRequest:
    out: ListNamedShadowsForThingRequest = {}  # type: ignore[typeddict-item]
    return out
