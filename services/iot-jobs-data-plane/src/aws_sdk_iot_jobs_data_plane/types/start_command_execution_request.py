"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#StartCommandExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_jobs_data_plane.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.client_request_token_v2
    import aws_sdk_iot_jobs_data_plane.types.command_arn
    import aws_sdk_iot_jobs_data_plane.types.command_execution_parameter_map
    import aws_sdk_iot_jobs_data_plane.types.command_execution_timeout_in_seconds
    import aws_sdk_iot_jobs_data_plane.types.target_arn


class StartCommandExecutionRequest(TypedDict, closed=True):
    target_arn: "aws_sdk_iot_jobs_data_plane.types.target_arn.TargetArn"
    """<p>The Amazon Resource Number (ARN) of the device where the command execution is occurring.</p>"""
    command_arn: "aws_sdk_iot_jobs_data_plane.types.command_arn.CommandArn"
    """<p>The Amazon Resource Number (ARN) of the command. For example, <code>arn:aws:iot:<region>:<accountid>:command/<commandName></code> </p>"""
    parameters: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.command_execution_parameter_map.CommandExecutionParameterMap"
    ]
    """<p>A list of parameters that are required by the <code>StartCommandExecution</code> API when performing the command on a device.</p>"""
    execution_timeout_seconds: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.command_execution_timeout_in_seconds.CommandExecutionTimeoutInSeconds"
    ]
    """<p>Specifies the amount of time in second the device has to finish the command execution. A timer is started as soon as the command execution is created. If the command execution status is not set to another terminal state before the timer expires, it will automatically update to <code>TIMED_OUT</code>.</p>"""
    client_token: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.client_request_token_v2.ClientRequestTokenV2"
    ]
    """<p>The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you retry the request using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, Amazon Web Services SDKs will automatically generate a unique client request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCommandExecutionRequest) -> dict:
    out: dict = {}
    out["targetArn"] = value["target_arn"]
    out["commandArn"] = value["command_arn"]
    if "parameters" in value:
        import aws_sdk_iot_jobs_data_plane.types.command_execution_parameter_map

        out["parameters"] = (
            aws_sdk_iot_jobs_data_plane.types.command_execution_parameter_map.serialize_json(
                value["parameters"]
            )
        )
    if "execution_timeout_seconds" in value:
        out["executionTimeoutSeconds"] = value["execution_timeout_seconds"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartCommandExecutionRequest:
    out: StartCommandExecutionRequest = {}  # type: ignore[typeddict-item]
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("StartCommandExecutionRequest.target_arn required")
    if "commandArn" in data:
        out["command_arn"] = data["commandArn"]
    else:
        raise DeserializationError("StartCommandExecutionRequest.command_arn required")
    if "parameters" in data:
        import aws_sdk_iot_jobs_data_plane.types.command_execution_parameter_map

        out["parameters"] = (
            aws_sdk_iot_jobs_data_plane.types.command_execution_parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    if "executionTimeoutSeconds" in data:
        out["execution_timeout_seconds"] = data["executionTimeoutSeconds"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
