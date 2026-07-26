"""Generated from Smithy shape ``com.amazonaws.apigateway#GatewayResponses``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_gateway_response
    import capo_api_gateway.types.string


class GatewayResponses(TypedDict, closed=True):
    items: NotRequired[
        "capo_api_gateway.types.list_of_gateway_response.ListOfGatewayResponse"
    ]
    """<p>Returns the entire collection, because of no pagination support.</p>"""
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set. The GatewayResponse collection does not support pagination and the position does not apply here.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayResponses) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_api_gateway.types.list_of_gateway_response

        out["item"] = capo_api_gateway.types.list_of_gateway_response.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> GatewayResponses:
    out: GatewayResponses = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import capo_api_gateway.types.list_of_gateway_response

        out["items"] = capo_api_gateway.types.list_of_gateway_response.deserialize_json(
            data["item"]
        )
    return out
