"""Generated from Smithy shape ``com.amazonaws.codebuild#StartCommandExecutionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.command_execution


class StartCommandExecutionOutput(TypedDict):
    command_execution: NotRequired[
        "aws_sdk_codebuild.types.command_execution.CommandExecution"
    ]
    """<p>Information about the requested command executions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCommandExecutionOutput) -> dict:
    out: dict = {}
    if "command_execution" in value:
        import aws_sdk_codebuild.types.command_execution

        out["commandExecution"] = (
            aws_sdk_codebuild.types.command_execution.serialize_aws_json_1_1(
                value["command_execution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCommandExecutionOutput:
    out: StartCommandExecutionOutput = {}  # type: ignore[typeddict-item]
    if "commandExecution" in data:
        import aws_sdk_codebuild.types.command_execution

        out["command_execution"] = (
            aws_sdk_codebuild.types.command_execution.deserialize_aws_json_1_1(
                data["commandExecution"]
            )
        )
    return out
