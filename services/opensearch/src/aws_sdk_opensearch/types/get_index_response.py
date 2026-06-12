"""Generated from Smithy shape ``com.amazonaws.opensearch#GetIndexResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.index_schema


class GetIndexResponse(TypedDict):
    index_schema: "aws_sdk_opensearch.types.index_schema.IndexSchema"
    """<p>The JSON schema of the index including mappings, settings, and semantic enrichment configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexResponse) -> dict:
    out: dict = {}
    out["IndexSchema"] = value["index_schema"]
    return out


def deserialize_json(data: dict) -> GetIndexResponse:
    out: GetIndexResponse = {}  # type: ignore[typeddict-item]
    if "IndexSchema" in data:
        out["index_schema"] = data["IndexSchema"]
    else:
        raise DeserializationError("GetIndexResponse.index_schema required")
    return out
