"""Generated from Smithy shape ``com.amazonaws.pipes#StopPipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.pipe_name


class StopPipeRequest(TypedDict, closed=True):
    name: "capo_pipes.types.pipe_name.PipeName"
    """<p>The name of the pipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopPipeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopPipeRequest:
    out: StopPipeRequest = {}  # type: ignore[typeddict-item]
    return out
