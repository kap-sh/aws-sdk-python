"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ReadJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.id


class ReadJobRequest(TypedDict):
    id: "aws_sdk_elastic_transcoder.types.id.Id"
    """<p>The identifier of the job for which you want to get detailed information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ReadJobRequest:
    out: ReadJobRequest = {}  # type: ignore[typeddict-item]
    return out
