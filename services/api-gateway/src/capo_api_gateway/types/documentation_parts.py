"""Generated from Smithy shape ``com.amazonaws.apigateway#DocumentationParts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_documentation_part
    import capo_api_gateway.types.string


class DocumentationParts(TypedDict, closed=True):
    items: NotRequired[
        "capo_api_gateway.types.list_of_documentation_part.ListOfDocumentationPart"
    ]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentationParts) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_api_gateway.types.list_of_documentation_part

        out["item"] = capo_api_gateway.types.list_of_documentation_part.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> DocumentationParts:
    out: DocumentationParts = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import capo_api_gateway.types.list_of_documentation_part

        out["items"] = (
            capo_api_gateway.types.list_of_documentation_part.deserialize_json(
                data["item"]
            )
        )
    return out
