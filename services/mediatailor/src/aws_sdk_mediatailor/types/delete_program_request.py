"""Generated from Smithy shape ``com.amazonaws.mediatailor#DeleteProgramRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DeleteProgramRequest(TypedDict, closed=True):
    channel_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the channel.</p>"""
    program_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the program.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProgramRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProgramRequest:
    out: DeleteProgramRequest = {}  # type: ignore[typeddict-item]
    return out
