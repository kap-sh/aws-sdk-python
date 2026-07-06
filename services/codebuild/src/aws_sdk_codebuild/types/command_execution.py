"""Generated from Smithy shape ``com.amazonaws.codebuild#CommandExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.command_type
    import aws_sdk_codebuild.types.logs_location
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.sensitive_non_empty_string
    import aws_sdk_codebuild.types.timestamp


class CommandExecution(TypedDict, closed=True):
    id: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the command execution.</p>"""
    sandbox_id: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>A <code>sandboxId</code>.</p>"""
    submit_time: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>When the command execution process was initially submitted, expressed in Unix time format.</p>"""
    start_time: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>When the command execution process started, expressed in Unix time format.</p>"""
    end_time: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>When the command execution process ended, expressed in Unix time format.</p>"""
    status: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The status of the command execution.</p>"""
    command: NotRequired[
        "aws_sdk_codebuild.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The command that needs to be executed.</p>"""
    type: NotRequired["aws_sdk_codebuild.types.command_type.CommandType"]
    """<p>The command type.</p>"""
    exit_code: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The exit code to return upon completion.</p>"""
    standard_output_content: NotRequired[
        "aws_sdk_codebuild.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The text written by the command to stdout.</p>"""
    standard_err_content: NotRequired[
        "aws_sdk_codebuild.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The text written by the command to stderr.</p>"""
    logs: NotRequired["aws_sdk_codebuild.types.logs_location.LogsLocation"]
    sandbox_arn: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>A <code>sandboxArn</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandExecution) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "sandbox_id" in value:
        out["sandboxId"] = value["sandbox_id"]
    if "submit_time" in value:
        import aws_sdk_codebuild.types.timestamp

        out["submitTime"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["submit_time"]
        )
    if "start_time" in value:
        import aws_sdk_codebuild.types.timestamp

        out["startTime"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_codebuild.types.timestamp

        out["endTime"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "command" in value:
        out["command"] = value["command"]
    if "type" in value:
        import aws_sdk_codebuild.types.command_type

        out["type"] = aws_sdk_codebuild.types.command_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "standard_output_content" in value:
        out["standardOutputContent"] = value["standard_output_content"]
    if "standard_err_content" in value:
        out["standardErrContent"] = value["standard_err_content"]
    if "logs" in value:
        import aws_sdk_codebuild.types.logs_location

        out["logs"] = aws_sdk_codebuild.types.logs_location.serialize_aws_json_1_1(
            value["logs"]
        )
    if "sandbox_arn" in value:
        out["sandboxArn"] = value["sandbox_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CommandExecution:
    out: CommandExecution = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "sandboxId" in data:
        out["sandbox_id"] = data["sandboxId"]
    if "submitTime" in data:
        import aws_sdk_codebuild.types.timestamp

        out["submit_time"] = aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["submitTime"]
        )
    if "startTime" in data:
        import aws_sdk_codebuild.types.timestamp

        out["start_time"] = aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_codebuild.types.timestamp

        out["end_time"] = aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if "status" in data:
        out["status"] = data["status"]
    if "command" in data:
        out["command"] = data["command"]
    if "type" in data:
        import aws_sdk_codebuild.types.command_type

        out["type"] = aws_sdk_codebuild.types.command_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "exitCode" in data:
        out["exit_code"] = data["exitCode"]
    if "standardOutputContent" in data:
        out["standard_output_content"] = data["standardOutputContent"]
    if "standardErrContent" in data:
        out["standard_err_content"] = data["standardErrContent"]
    if "logs" in data:
        import aws_sdk_codebuild.types.logs_location

        out["logs"] = aws_sdk_codebuild.types.logs_location.deserialize_aws_json_1_1(
            data["logs"]
        )
    if "sandboxArn" in data:
        out["sandbox_arn"] = data["sandboxArn"]
    return out
