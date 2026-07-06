"""Generated from Smithy shape ``com.amazonaws.codebuild#ListCommandExecutionsForSandboxOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.command_executions
    import aws_sdk_codebuild.types.string


class ListCommandExecutionsForSandboxOutput(TypedDict, closed=True):
    command_executions: NotRequired[
        "aws_sdk_codebuild.types.command_executions.CommandExecutions"
    ]
    """<p>Information about the requested command executions.</p>"""
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>Information about the next token to get paginated results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommandExecutionsForSandboxOutput) -> dict:
    out: dict = {}
    if "command_executions" in value:
        import aws_sdk_codebuild.types.command_executions

        out["commandExecutions"] = (
            aws_sdk_codebuild.types.command_executions.serialize_aws_json_1_1(
                value["command_executions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCommandExecutionsForSandboxOutput:
    out: ListCommandExecutionsForSandboxOutput = {}  # type: ignore[typeddict-item]
    if "commandExecutions" in data:
        import aws_sdk_codebuild.types.command_executions

        out["command_executions"] = (
            aws_sdk_codebuild.types.command_executions.deserialize_aws_json_1_1(
                data["commandExecutions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
