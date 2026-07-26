"""Generated from Smithy shape ``com.amazonaws.apigateway#RestApis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_rest_api
    import capo_api_gateway.types.string


class RestApis(TypedDict, closed=True):
    items: NotRequired["capo_api_gateway.types.list_of_rest_api.ListOfRestApi"]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestApis) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_api_gateway.types.list_of_rest_api

        out["item"] = capo_api_gateway.types.list_of_rest_api.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> RestApis:
    out: RestApis = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import capo_api_gateway.types.list_of_rest_api

        out["items"] = capo_api_gateway.types.list_of_rest_api.deserialize_json(
            data["item"]
        )
    return out
