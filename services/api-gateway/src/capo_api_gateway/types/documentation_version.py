"""Generated from Smithy shape ``com.amazonaws.apigateway#DocumentationVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string
    import capo_api_gateway.types.timestamp


class DocumentationVersion(TypedDict, closed=True):
    version: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The version identifier of the API documentation snapshot.</p>"""
    created_date: NotRequired["capo_api_gateway.types.timestamp.Timestamp"]
    """<p>The date when the API documentation snapshot is created.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The description of the API documentation snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentationVersion) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    if "created_date" in value:
        import capo_api_gateway.types.timestamp

        out["createdDate"] = capo_api_gateway.types.timestamp.serialize_json(
            value["created_date"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> DocumentationVersion:
    out: DocumentationVersion = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    if "createdDate" in data:
        import capo_api_gateway.types.timestamp

        out["created_date"] = capo_api_gateway.types.timestamp.deserialize_json(
            data["createdDate"]
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
