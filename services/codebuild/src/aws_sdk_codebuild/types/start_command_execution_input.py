"""Generated from Smithy shape ``com.amazonaws.codebuild#StartCommandExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.command_type
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.sensitive_non_empty_string


class StartCommandExecutionInput(TypedDict):
    sandbox_id: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p>A <code>sandboxId</code> or <code>sandboxArn</code>.</p>"""
    command: (
        "aws_sdk_codebuild.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>The command that needs to be executed.</p>"""
    type: NotRequired["aws_sdk_codebuild.types.command_type.CommandType"]
    """<p>The command type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCommandExecutionInput) -> dict:
    out: dict = {}
    out["sandboxId"] = value["sandbox_id"]
    out["command"] = value["command"]
    if "type" in value:
        import aws_sdk_codebuild.types.command_type

        out["type"] = aws_sdk_codebuild.types.command_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCommandExecutionInput:
    out: StartCommandExecutionInput = {}  # type: ignore[typeddict-item]
    if "sandboxId" in data:
        out["sandbox_id"] = data["sandboxId"]
    else:
        raise DeserializationError("StartCommandExecutionInput.sandbox_id required")
    if "command" in data:
        out["command"] = data["command"]
    else:
        raise DeserializationError("StartCommandExecutionInput.command required")
    if "type" in data:
        import aws_sdk_codebuild.types.command_type

        out["type"] = aws_sdk_codebuild.types.command_type.deserialize_aws_json_1_1(
            data["type"]
        )
    return out
