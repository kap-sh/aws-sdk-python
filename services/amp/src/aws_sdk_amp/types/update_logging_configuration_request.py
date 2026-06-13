"""Generated from Smithy shape ``com.amazonaws.amp#UpdateLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.log_group_arn
    import aws_sdk_amp.types.workspace_id


class UpdateLoggingConfigurationRequest(TypedDict):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to update the logging configuration for.</p>"""
    log_group_arn: "aws_sdk_amp.types.log_group_arn.LogGroupArn"
    """<p>The ARN of the CloudWatch log group to which the vended log data will be published.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLoggingConfigurationRequest) -> dict:
    out: dict = {}
    out["logGroupArn"] = value["log_group_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateLoggingConfigurationRequest:
    out: UpdateLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "logGroupArn" in data:
        out["log_group_arn"] = data["logGroupArn"]
    else:
        raise DeserializationError(
            "UpdateLoggingConfigurationRequest.log_group_arn required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
