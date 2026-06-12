"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetCommandExecutionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.command_execution_ids
    import aws_sdk_codebuild.types.command_executions


class BatchGetCommandExecutionsOutput(TypedDict):
    command_executions: NotRequired[
        "aws_sdk_codebuild.types.command_executions.CommandExecutions"
    ]
    """<p>Information about the requested command executions.</p>"""
    command_executions_not_found: NotRequired[
        "aws_sdk_codebuild.types.command_execution_ids.CommandExecutionIds"
    ]
    """<p>The IDs of command executions for which information could not be found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCommandExecutionsOutput) -> dict:
    out: dict = {}
    if "command_executions" in value:
        import aws_sdk_codebuild.types.command_executions

        out["commandExecutions"] = (
            aws_sdk_codebuild.types.command_executions.serialize_aws_json_1_1(
                value["command_executions"]
            )
        )
    if "command_executions_not_found" in value:
        import aws_sdk_codebuild.types.command_execution_ids

        out["commandExecutionsNotFound"] = (
            aws_sdk_codebuild.types.command_execution_ids.serialize_aws_json_1_1(
                value["command_executions_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCommandExecutionsOutput:
    out: BatchGetCommandExecutionsOutput = {}  # type: ignore[typeddict-item]
    if "commandExecutions" in data:
        import aws_sdk_codebuild.types.command_executions

        out["command_executions"] = (
            aws_sdk_codebuild.types.command_executions.deserialize_aws_json_1_1(
                data["commandExecutions"]
            )
        )
    if "commandExecutionsNotFound" in data:
        import aws_sdk_codebuild.types.command_execution_ids

        out["command_executions_not_found"] = (
            aws_sdk_codebuild.types.command_execution_ids.deserialize_aws_json_1_1(
                data["commandExecutionsNotFound"]
            )
        )
    return out
