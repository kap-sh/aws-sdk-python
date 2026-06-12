"""Generated from Smithy shape ``com.amazonaws.apigateway#RestApis``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_rest_api
    import aws_sdk_api_gateway.types.string


class RestApis(TypedDict):
    items: NotRequired["aws_sdk_api_gateway.types.list_of_rest_api.ListOfRestApi"]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestApis) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_api_gateway.types.list_of_rest_api

        out["item"] = aws_sdk_api_gateway.types.list_of_rest_api.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> RestApis:
    out: RestApis = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_rest_api

        out["items"] = aws_sdk_api_gateway.types.list_of_rest_api.deserialize_json(
            data["item"]
        )
    return out
