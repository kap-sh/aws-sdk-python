"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeInterpreterSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_arn
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_id
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_status
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.sandbox_name


class CodeInterpreterSummary(TypedDict, closed=True):
    code_interpreter_id: (
        "aws_sdk_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId"
    )
    """<p>The unique identifier of the code interpreter.</p>"""
    code_interpreter_arn: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_arn.CodeInterpreterArn"
    """<p>The Amazon Resource Name (ARN) of the code interpreter.</p>"""
    name: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.sandbox_name.SandboxName"
    ]
    """<p>The name of the code interpreter.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the code interpreter.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_status.CodeInterpreterStatus"
    """<p>The current status of the code interpreter.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the code interpreter was created.</p>"""
    last_updated_at: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when the code interpreter was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterSummary) -> dict:
    out: dict = {}
    out["codeInterpreterId"] = value["code_interpreter_id"]
    out["codeInterpreterArn"] = value["code_interpreter_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.code_interpreter_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    if "last_updated_at" in value:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodeInterpreterSummary:
    out: CodeInterpreterSummary = {}  # type: ignore[typeddict-item]
    if "codeInterpreterId" in data:
        out["code_interpreter_id"] = data["codeInterpreterId"]
    else:
        raise DeserializationError(
            "CodeInterpreterSummary.code_interpreter_id required"
        )
    if "codeInterpreterArn" in data:
        out["code_interpreter_arn"] = data["codeInterpreterArn"]
    else:
        raise DeserializationError(
            "CodeInterpreterSummary.code_interpreter_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.code_interpreter_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.code_interpreter_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CodeInterpreterSummary.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CodeInterpreterSummary.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
