"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetSchemaAsJsonResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.schema_json_document
    import capo_clouddirectory.types.schema_name


class GetSchemaAsJsonResponse(TypedDict, closed=True):
    name: NotRequired["capo_clouddirectory.types.schema_name.SchemaName"]
    """<p>The name of the retrieved schema.</p>"""
    document: NotRequired[
        "capo_clouddirectory.types.schema_json_document.SchemaJsonDocument"
    ]
    """<p>The JSON representation of the schema document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaAsJsonResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "document" in value:
        out["Document"] = value["document"]
    return out


def deserialize_json(data: dict) -> GetSchemaAsJsonResponse:
    out: GetSchemaAsJsonResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Document" in data:
        out["document"] = data["Document"]
    return out
