"""Generated from Smithy shape ``com.amazonaws.apigateway#VpcLinks``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_vpc_link
    import capo_api_gateway.types.string


class VpcLinks(TypedDict, closed=True):
    items: NotRequired["capo_api_gateway.types.list_of_vpc_link.ListOfVpcLink"]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcLinks) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_api_gateway.types.list_of_vpc_link

        out["item"] = capo_api_gateway.types.list_of_vpc_link.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> VpcLinks:
    out: VpcLinks = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import capo_api_gateway.types.list_of_vpc_link

        out["items"] = capo_api_gateway.types.list_of_vpc_link.deserialize_json(
            data["item"]
        )
    return out
