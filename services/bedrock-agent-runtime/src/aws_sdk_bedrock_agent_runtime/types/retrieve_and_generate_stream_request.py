"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateStreamRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration
    import aws_sdk_bedrock_agent_runtime.types.session_id


class RetrieveAndGenerateStreamRequest(TypedDict):
    session_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"]
    """<p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>"""
    input: "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input.RetrieveAndGenerateInput"
    """<p>Contains the query to be made to the knowledge base.</p>"""
    retrieve_and_generate_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"
    ]
    r"""<p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>"""
    session_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.RetrieveAndGenerateSessionConfiguration"
    ]
    """<p>Contains details about the session with the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateStreamRequest) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input

    out["input"] = (
        aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input.serialize_json(
            value["input"]
        )
    )
    if "retrieve_and_generate_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration

        out["retrieveAndGenerateConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration.serialize_json(
                value["retrieve_and_generate_configuration"]
            )
        )
    if "session_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration

        out["sessionConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.serialize_json(
                value["session_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrieveAndGenerateStreamRequest:
    out: RetrieveAndGenerateStreamRequest = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "input" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input

        out["input"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input.deserialize_json(
                data["input"]
            )
        )
    else:
        raise DeserializationError("RetrieveAndGenerateStreamRequest.input required")
    if "retrieveAndGenerateConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration

        out["retrieve_and_generate_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration.deserialize_json(
                data["retrieveAndGenerateConfiguration"]
            )
        )
    if "sessionConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration

        out["session_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.deserialize_json(
                data["sessionConfiguration"]
            )
        )
    return out
