"""Generated from Smithy shape ``com.amazonaws.iot#GetCommandExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.boolean_wrapper_object
    import aws_sdk_iot.types.command_execution_id
    import aws_sdk_iot.types.target_arn


class GetCommandExecutionRequest(TypedDict):
    execution_id: "aws_sdk_iot.types.command_execution_id.CommandExecutionId"
    """<p>The unique identifier for the command execution. This information is returned as a response of the <code>StartCommandExecution</code> API request.</p>"""
    target_arn: "aws_sdk_iot.types.target_arn.TargetArn"
    """<p>The Amazon Resource Number (ARN) of the device on which the command execution is being performed.</p>"""
    include_result: NotRequired[
        "aws_sdk_iot.types.boolean_wrapper_object.BooleanWrapperObject"
    ]
    """<p>Can be used to specify whether to include the result of the command execution in the <code>GetCommandExecution</code> API response. Your device can use this field to provide additional information about the command execution. You only need to specify this field when using the <code>AWS-IoT</code> namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCommandExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCommandExecutionRequest:
    out: GetCommandExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
