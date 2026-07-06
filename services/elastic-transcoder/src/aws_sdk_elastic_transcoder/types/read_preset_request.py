"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ReadPresetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.id


class ReadPresetRequest(TypedDict, closed=True):
    id: "aws_sdk_elastic_transcoder.types.id.Id"
    """<p>The identifier of the preset for which you want to get detailed information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadPresetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ReadPresetRequest:
    out: ReadPresetRequest = {}  # type: ignore[typeddict-item]
    return out
