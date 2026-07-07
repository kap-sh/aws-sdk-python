"""Generated from Smithy shape ``com.amazonaws.apigateway#Authorizers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_authorizer
    import aws_sdk_api_gateway.types.string


class Authorizers(TypedDict, closed=True):
    items: NotRequired["aws_sdk_api_gateway.types.list_of_authorizer.ListOfAuthorizer"]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Authorizers) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_api_gateway.types.list_of_authorizer

        out["item"] = aws_sdk_api_gateway.types.list_of_authorizer.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> Authorizers:
    out: Authorizers = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_authorizer

        out["items"] = aws_sdk_api_gateway.types.list_of_authorizer.deserialize_json(
            data["item"]
        )
    return out
