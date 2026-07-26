"""Generated from Smithy shape ``com.amazonaws.iot#DeleteStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.stream_id


class DeleteStreamRequest(TypedDict, closed=True):
    stream_id: "capo_iot.types.stream_id.StreamId"
    """<p>The stream ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStreamRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteStreamRequest:
    out: DeleteStreamRequest = {}  # type: ignore[typeddict-item]
    return out
