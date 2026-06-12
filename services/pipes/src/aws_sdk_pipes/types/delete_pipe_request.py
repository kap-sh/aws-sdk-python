"""Generated from Smithy shape ``com.amazonaws.pipes#DeletePipeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.pipe_name


class DeletePipeRequest(TypedDict):
    name: "aws_sdk_pipes.types.pipe_name.PipeName"
    """<p>The name of the pipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePipeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePipeRequest:
    out: DeletePipeRequest = {}  # type: ignore[typeddict-item]
    return out
