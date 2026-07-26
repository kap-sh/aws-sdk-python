"""Generated from Smithy shape ``com.amazonaws.schemas#GetDiscoveredSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string


class GetDiscoveredSchemaResponse(TypedDict, closed=True):
    content: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The source of the schema definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDiscoveredSchemaResponse) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    return out


def deserialize_json(data: dict) -> GetDiscoveredSchemaResponse:
    out: GetDiscoveredSchemaResponse = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    return out
