"""Generated from Smithy shape ``com.amazonaws.iot#DeleteCommandRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_id


class DeleteCommandRequest(TypedDict, closed=True):
    command_id: "aws_sdk_iot.types.command_id.CommandId"
    """<p>The unique identifier of the command to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCommandRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCommandRequest:
    out: DeleteCommandRequest = {}  # type: ignore[typeddict-item]
    return out
