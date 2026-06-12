"""Generated from Smithy shape ``com.amazonaws.pipes#DescribePipeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.pipe_name


class DescribePipeRequest(TypedDict):
    name: "aws_sdk_pipes.types.pipe_name.PipeName"
    """<p>The name of the pipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePipeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePipeRequest:
    out: DescribePipeRequest = {}  # type: ignore[typeddict-item]
    return out
