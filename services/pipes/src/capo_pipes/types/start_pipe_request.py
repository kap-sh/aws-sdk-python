"""Generated from Smithy shape ``com.amazonaws.pipes#StartPipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.pipe_name


class StartPipeRequest(TypedDict, closed=True):
    name: "capo_pipes.types.pipe_name.PipeName"
    """<p>The name of the pipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPipeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartPipeRequest:
    out: StartPipeRequest = {}  # type: ignore[typeddict-item]
    return out
