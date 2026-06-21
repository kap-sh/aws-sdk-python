"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CitationEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.citation
    import aws_sdk_bedrock_agent_runtime.types.generated_response_part
    import aws_sdk_bedrock_agent_runtime.types.retrieved_references


class CitationEvent(TypedDict):
    citation: NotRequired["aws_sdk_bedrock_agent_runtime.types.citation.Citation"]
    """<p>The citation.</p>"""
    generated_response_part: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.generated_response_part.GeneratedResponsePart"
    ]
    """<p>The generated response to the citation event.</p>"""
    retrieved_references: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieved_references.RetrievedReferences"
    ]
    """<p>The retrieved references of the citation event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CitationEvent) -> dict:
    out: dict = {}
    if "citation" in value:
        import aws_sdk_bedrock_agent_runtime.types.citation

        out["citation"] = aws_sdk_bedrock_agent_runtime.types.citation.serialize_json(
            value["citation"]
        )
    if "generated_response_part" in value:
        import aws_sdk_bedrock_agent_runtime.types.generated_response_part

        out["generatedResponsePart"] = (
            aws_sdk_bedrock_agent_runtime.types.generated_response_part.serialize_json(
                value["generated_response_part"]
            )
        )
    if "retrieved_references" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieved_references

        out["retrievedReferences"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieved_references.serialize_json(
                value["retrieved_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> CitationEvent:
    out: CitationEvent = {}  # type: ignore[typeddict-item]
    if "citation" in data:
        import aws_sdk_bedrock_agent_runtime.types.citation

        out["citation"] = aws_sdk_bedrock_agent_runtime.types.citation.deserialize_json(
            data["citation"]
        )
    if "generatedResponsePart" in data:
        import aws_sdk_bedrock_agent_runtime.types.generated_response_part

        out["generated_response_part"] = (
            aws_sdk_bedrock_agent_runtime.types.generated_response_part.deserialize_json(
                data["generatedResponsePart"]
            )
        )
    if "retrievedReferences" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieved_references

        out["retrieved_references"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieved_references.deserialize_json(
                data["retrievedReferences"]
            )
        )
    return out


def serialize_event_json(value: CitationEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "citation"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> CitationEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: CitationEvent = {}  # type: ignore[typeddict-item]
    return out
