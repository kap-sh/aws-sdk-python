"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#UpdatePipelineStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.pipeline


class UpdatePipelineStatusResponse(TypedDict, closed=True):
    pipeline: NotRequired["aws_sdk_elastic_transcoder.types.pipeline.Pipeline"]
    """<p>A section of the response body that provides information about the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePipelineStatusResponse) -> dict:
    out: dict = {}
    if "pipeline" in value:
        import aws_sdk_elastic_transcoder.types.pipeline

        out["Pipeline"] = aws_sdk_elastic_transcoder.types.pipeline.serialize_json(
            value["pipeline"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePipelineStatusResponse:
    out: UpdatePipelineStatusResponse = {}  # type: ignore[typeddict-item]
    if "Pipeline" in data:
        import aws_sdk_elastic_transcoder.types.pipeline

        out["pipeline"] = aws_sdk_elastic_transcoder.types.pipeline.deserialize_json(
            data["Pipeline"]
        )
    return out
