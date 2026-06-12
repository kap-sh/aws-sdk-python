"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ReadPipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.id


class ReadPipelineRequest(TypedDict):
    id: "aws_sdk_elastic_transcoder.types.id.Id"
    """<p>The identifier of the pipeline to read.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadPipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ReadPipelineRequest:
    out: ReadPipelineRequest = {}  # type: ignore[typeddict-item]
    return out
