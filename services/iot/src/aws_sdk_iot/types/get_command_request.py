"""Generated from Smithy shape ``com.amazonaws.iot#GetCommandRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_id


class GetCommandRequest(TypedDict):
    command_id: "aws_sdk_iot.types.command_id.CommandId"
    """<p>The unique identifier of the command for which you want to retrieve information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCommandRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCommandRequest:
    out: GetCommandRequest = {}  # type: ignore[typeddict-item]
    return out
