"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListRouterInputsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_filter_list


class ListRouterInputsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of router inputs to return in the response.</p>"""
    next_token: NotRequired["str"]
    """<p>A token used to retrieve the next page of results.</p>"""
    filters: NotRequired[
        "capo_mediaconnect.types.router_input_filter_list.RouterInputFilterList"
    ]
    """<p>The filters to apply when retrieving the list of router inputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRouterInputsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_mediaconnect.types.router_input_filter_list

        out["filters"] = (
            capo_mediaconnect.types.router_input_filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRouterInputsRequest:
    out: ListRouterInputsRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_mediaconnect.types.router_input_filter_list

        out["filters"] = (
            capo_mediaconnect.types.router_input_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out
