"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseLookupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.metadata
    import aws_sdk_bedrock_agent_runtime.types.retrieved_references


class KnowledgeBaseLookupOutput(TypedDict):
    retrieved_references: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieved_references.RetrievedReferences"
    ]
    """<p>Contains metadata about the sources cited for the generated response.</p>"""
    metadata: NotRequired["aws_sdk_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>Contains information about the knowledge base output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseLookupOutput) -> dict:
    out: dict = {}
    if "retrieved_references" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieved_references

        out["retrievedReferences"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieved_references.serialize_json(
                value["retrieved_references"]
            )
        )
    if "metadata" in value:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseLookupOutput:
    out: KnowledgeBaseLookupOutput = {}  # type: ignore[typeddict-item]
    if "retrievedReferences" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieved_references

        out["retrieved_references"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieved_references.deserialize_json(
                data["retrievedReferences"]
            )
        )
    if "metadata" in data:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    return out
