"""Generated from Smithy shape ``com.amazonaws.apigateway#VpcLinks``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_vpc_link
    import aws_sdk_api_gateway.types.string


class VpcLinks(TypedDict):
    items: NotRequired["aws_sdk_api_gateway.types.list_of_vpc_link.ListOfVpcLink"]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcLinks) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_api_gateway.types.list_of_vpc_link

        out["item"] = aws_sdk_api_gateway.types.list_of_vpc_link.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> VpcLinks:
    out: VpcLinks = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_vpc_link

        out["items"] = aws_sdk_api_gateway.types.list_of_vpc_link.deserialize_json(
            data["item"]
        )
    return out
