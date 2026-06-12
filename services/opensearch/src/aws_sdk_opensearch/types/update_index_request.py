"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.index_name
    import aws_sdk_opensearch.types.index_schema


class UpdateIndexRequest(TypedDict):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    index_name: "aws_sdk_opensearch.types.index_name.IndexName"
    """<p>The name of the index to update.</p>"""
    index_schema: "aws_sdk_opensearch.types.index_schema.IndexSchema"
    """<p>The updated JSON schema for the index including any changes to mappings, settings, and semantic enrichment configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexRequest) -> dict:
    out: dict = {}
    out["IndexSchema"] = value["index_schema"]
    return out


def deserialize_json(data: dict) -> UpdateIndexRequest:
    out: UpdateIndexRequest = {}  # type: ignore[typeddict-item]
    if "IndexSchema" in data:
        out["index_schema"] = data["IndexSchema"]
    else:
        raise DeserializationError("UpdateIndexRequest.index_schema required")
    return out
