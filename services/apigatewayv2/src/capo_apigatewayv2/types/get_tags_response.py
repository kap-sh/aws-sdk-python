"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.tags


class GetTagsResponse(TypedDict, closed=True):
    tags: NotRequired["capo_apigatewayv2.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: GetTagsResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_apigatewayv2.types.tags

        out["tags"] = capo_apigatewayv2.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetTagsResponse:
    out: GetTagsResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_apigatewayv2.types.tags

        out["tags"] = capo_apigatewayv2.types.tags.deserialize_json(data["tags"])
    return out
