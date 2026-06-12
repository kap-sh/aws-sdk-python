"""Generated from Smithy shape ``com.amazonaws.apigateway#DocumentationVersions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_documentation_version
    import aws_sdk_api_gateway.types.string


class DocumentationVersions(TypedDict):
    items: NotRequired[
        "aws_sdk_api_gateway.types.list_of_documentation_version.ListOfDocumentationVersion"
    ]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentationVersions) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_api_gateway.types.list_of_documentation_version

        out["item"] = (
            aws_sdk_api_gateway.types.list_of_documentation_version.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentationVersions:
    out: DocumentationVersions = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_documentation_version

        out["items"] = (
            aws_sdk_api_gateway.types.list_of_documentation_version.deserialize_json(
                data["item"]
            )
        )
    return out
