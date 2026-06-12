"""Generated from Smithy shape ``com.amazonaws.apigateway#Resources``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_resource
    import aws_sdk_api_gateway.types.string


class Resources(TypedDict):
    items: NotRequired["aws_sdk_api_gateway.types.list_of_resource.ListOfResource"]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resources) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_api_gateway.types.list_of_resource

        out["item"] = aws_sdk_api_gateway.types.list_of_resource.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> Resources:
    out: Resources = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_resource

        out["items"] = aws_sdk_api_gateway.types.list_of_resource.deserialize_json(
            data["item"]
        )
    return out
