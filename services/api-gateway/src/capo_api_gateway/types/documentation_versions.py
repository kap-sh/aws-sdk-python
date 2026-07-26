"""Generated from Smithy shape ``com.amazonaws.apigateway#DocumentationVersions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_documentation_version
    import capo_api_gateway.types.string


class DocumentationVersions(TypedDict, closed=True):
    items: NotRequired[
        "capo_api_gateway.types.list_of_documentation_version.ListOfDocumentationVersion"
    ]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentationVersions) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_api_gateway.types.list_of_documentation_version

        out["item"] = (
            capo_api_gateway.types.list_of_documentation_version.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentationVersions:
    out: DocumentationVersions = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import capo_api_gateway.types.list_of_documentation_version

        out["items"] = (
            capo_api_gateway.types.list_of_documentation_version.deserialize_json(
                data["item"]
            )
        )
    return out
