"""Generated from Smithy shape ``com.amazonaws.schemas#GetDiscoveredSchemaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string


class GetDiscoveredSchemaResponse(TypedDict):
    content: NotRequired["aws_sdk_schemas.types.__string.__string"]
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
