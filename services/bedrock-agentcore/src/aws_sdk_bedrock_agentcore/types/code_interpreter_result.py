"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CodeInterpreterResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.content_block_list
    import aws_sdk_bedrock_agentcore.types.tool_result_structured_content

class CodeInterpreterResult(TypedDict):
    content: "aws_sdk_bedrock_agentcore.types.content_block_list.ContentBlockList"
    """<p>The textual content of the execution result. This includes standard output from the code execution, such as print statements, console output, and text representations of results.</p>"""
    structured_content: NotRequired["aws_sdk_bedrock_agentcore.types.tool_result_structured_content.ToolResultStructuredContent"]
    """<p>The structured content of the execution result. This includes additional metadata about the execution, such as execution time, memory usage, and structured representations of output data. The format depends on the specific code interpreter and execution context.</p>"""
    is_error: NotRequired["bool"]
    """<p>Indicates whether the result represents an error. If true, the content contains error messages or exception information. If false, the content contains successful execution results.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterResult) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.content_block_list
    out["content"] = aws_sdk_bedrock_agentcore.types.content_block_list.serialize_json(value["content"])
    if "structured_content" in value:
        import aws_sdk_bedrock_agentcore.types.tool_result_structured_content
        out["structuredContent"] = aws_sdk_bedrock_agentcore.types.tool_result_structured_content.serialize_json(value["structured_content"])
    if "is_error" in value:
        out["isError"] = value["is_error"]
    return out


def deserialize_json(data: dict) -> CodeInterpreterResult:
    out: CodeInterpreterResult = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import aws_sdk_bedrock_agentcore.types.content_block_list
        out["content"] = aws_sdk_bedrock_agentcore.types.content_block_list.deserialize_json(data["content"])
    else:
        raise DeserializationError("CodeInterpreterResult.content required")
    if "structuredContent" in data:
        import aws_sdk_bedrock_agentcore.types.tool_result_structured_content
        out["structured_content"] = aws_sdk_bedrock_agentcore.types.tool_result_structured_content.deserialize_json(data["structuredContent"])
    if "isError" in data:
        out["is_error"] = data["isError"]
    return out