"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DocumentIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.document_identifier

DocumentIdentifiers: TypeAlias = list[
    "capo_bedrock_agent.types.document_identifier.DocumentIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentIdentifiers) -> list:
    import capo_bedrock_agent.types.document_identifier

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.document_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentIdentifiers:
    import capo_bedrock_agent.types.document_identifier

    out: DocumentIdentifiers = []
    for item in data:
        out.append(capo_bedrock_agent.types.document_identifier.deserialize_json(item))
    return out
