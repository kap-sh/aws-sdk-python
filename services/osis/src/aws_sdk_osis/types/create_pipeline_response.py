"""Generated from Smithy shape ``com.amazonaws.osis#CreatePipelineResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline


class CreatePipelineResponse(TypedDict):
    pipeline: NotRequired["aws_sdk_osis.types.pipeline.Pipeline"]
    """<p>Container for information about the created pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePipelineResponse) -> dict:
    out: dict = {}
    if "pipeline" in value:
        import aws_sdk_osis.types.pipeline

        out["Pipeline"] = aws_sdk_osis.types.pipeline.serialize_json(value["pipeline"])
    return out


def deserialize_json(data: dict) -> CreatePipelineResponse:
    out: CreatePipelineResponse = {}  # type: ignore[typeddict-item]
    if "Pipeline" in data:
        import aws_sdk_osis.types.pipeline

        out["pipeline"] = aws_sdk_osis.types.pipeline.deserialize_json(data["Pipeline"])
    return out
