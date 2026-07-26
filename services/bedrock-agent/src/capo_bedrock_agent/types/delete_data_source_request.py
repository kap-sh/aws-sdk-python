"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id


class DeleteDataSourceRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base from which to delete the data source.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataSourceRequest:
    out: DeleteDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
