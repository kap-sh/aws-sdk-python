"""Generated from Smithy shape ``com.amazonaws.apigateway#BasePathMappings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_base_path_mapping
    import aws_sdk_api_gateway.types.string


class BasePathMappings(TypedDict):
    items: NotRequired[
        "aws_sdk_api_gateway.types.list_of_base_path_mapping.ListOfBasePathMapping"
    ]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasePathMappings) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_api_gateway.types.list_of_base_path_mapping

        out["item"] = (
            aws_sdk_api_gateway.types.list_of_base_path_mapping.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> BasePathMappings:
    out: BasePathMappings = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_base_path_mapping

        out["items"] = (
            aws_sdk_api_gateway.types.list_of_base_path_mapping.deserialize_json(
                data["item"]
            )
        )
    return out
