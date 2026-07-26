"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id


class GetDataSourceRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base for the data source.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataSourceRequest:
    out: GetDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
