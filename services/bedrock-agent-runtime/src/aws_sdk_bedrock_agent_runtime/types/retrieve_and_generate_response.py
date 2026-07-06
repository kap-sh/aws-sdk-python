"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.citations
    import aws_sdk_bedrock_agent_runtime.types.guadrail_action
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output
    import aws_sdk_bedrock_agent_runtime.types.session_id


class RetrieveAndGenerateResponse(TypedDict, closed=True):
    session_id: "aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"
    """<p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>"""
    output: "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output.RetrieveAndGenerateOutput"
    """<p>Contains the response generated from querying the knowledge base.</p>"""
    citations: NotRequired["aws_sdk_bedrock_agent_runtime.types.citations.Citations"]
    """<p>A list of segments of the generated response that are based on sources in the knowledge base, alongside information about the sources.</p>"""
    guardrail_action: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guadrail_action.GuadrailAction"
    ]
    """<p>Specifies if there is a guardrail intervention in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateResponse) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output

    out["output"] = (
        aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output.serialize_json(
            value["output"]
        )
    )
    if "citations" in value:
        import aws_sdk_bedrock_agent_runtime.types.citations

        out["citations"] = aws_sdk_bedrock_agent_runtime.types.citations.serialize_json(
            value["citations"]
        )
    if "guardrail_action" in value:
        import aws_sdk_bedrock_agent_runtime.types.guadrail_action

        out["guardrailAction"] = (
            aws_sdk_bedrock_agent_runtime.types.guadrail_action.serialize_json(
                value["guardrail_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrieveAndGenerateResponse:
    out: RetrieveAndGenerateResponse = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("RetrieveAndGenerateResponse.session_id required")
    if "output" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output

        out["output"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_output.deserialize_json(
                data["output"]
            )
        )
    else:
        raise DeserializationError("RetrieveAndGenerateResponse.output required")
    if "citations" in data:
        import aws_sdk_bedrock_agent_runtime.types.citations

        out["citations"] = (
            aws_sdk_bedrock_agent_runtime.types.citations.deserialize_json(
                data["citations"]
            )
        )
    if "guardrailAction" in data:
        import aws_sdk_bedrock_agent_runtime.types.guadrail_action

        out["guardrail_action"] = (
            aws_sdk_bedrock_agent_runtime.types.guadrail_action.deserialize_json(
                data["guardrailAction"]
            )
        )
    return out
