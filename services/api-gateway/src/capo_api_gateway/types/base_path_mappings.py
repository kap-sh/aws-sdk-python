"""Generated from Smithy shape ``com.amazonaws.apigateway#BasePathMappings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_base_path_mapping
    import capo_api_gateway.types.string


class BasePathMappings(TypedDict, closed=True):
    items: NotRequired[
        "capo_api_gateway.types.list_of_base_path_mapping.ListOfBasePathMapping"
    ]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasePathMappings) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_api_gateway.types.list_of_base_path_mapping

        out["item"] = capo_api_gateway.types.list_of_base_path_mapping.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> BasePathMappings:
    out: BasePathMappings = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import capo_api_gateway.types.list_of_base_path_mapping

        out["items"] = (
            capo_api_gateway.types.list_of_base_path_mapping.deserialize_json(
                data["item"]
            )
        )
    return out
