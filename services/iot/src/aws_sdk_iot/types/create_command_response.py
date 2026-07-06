"""Generated from Smithy shape ``com.amazonaws.iot#CreateCommandResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_arn
    import aws_sdk_iot.types.command_id


class CreateCommandResponse(TypedDict, closed=True):
    command_id: NotRequired["aws_sdk_iot.types.command_id.CommandId"]
    """<p>The unique identifier for the command.</p>"""
    command_arn: NotRequired["aws_sdk_iot.types.command_arn.CommandArn"]
    """<p>The Amazon Resource Number (ARN) of the command. For example, <code>arn:aws:iot:<region>:<accountid>:command/<commandId></code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCommandResponse) -> dict:
    out: dict = {}
    if "command_id" in value:
        out["commandId"] = value["command_id"]
    if "command_arn" in value:
        out["commandArn"] = value["command_arn"]
    return out


def deserialize_json(data: dict) -> CreateCommandResponse:
    out: CreateCommandResponse = {}  # type: ignore[typeddict-item]
    if "commandId" in data:
        out["command_id"] = data["commandId"]
    if "commandArn" in data:
        out["command_arn"] = data["commandArn"]
    return out
