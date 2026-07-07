"""Generated from Smithy shape ``com.amazonaws.mediatailor#DescribeProgramRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DescribeProgramRequest(TypedDict, closed=True):
    channel_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the channel associated with this Program.</p>"""
    program_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the program.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProgramRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeProgramRequest:
    out: DescribeProgramRequest = {}  # type: ignore[typeddict-item]
    return out
