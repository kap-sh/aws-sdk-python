"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#DeletePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.id


class DeletePipelineRequest(TypedDict, closed=True):
    id: "capo_elastic_transcoder.types.id.Id"
    """<p>The identifier of the pipeline that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePipelineRequest:
    out: DeletePipelineRequest = {}  # type: ignore[typeddict-item]
    return out
