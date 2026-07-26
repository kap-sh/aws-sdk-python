"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CreatePipelineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.pipeline
    import capo_elastic_transcoder.types.warnings


class CreatePipelineResponse(TypedDict, closed=True):
    pipeline: NotRequired["capo_elastic_transcoder.types.pipeline.Pipeline"]
    """<p>A section of the response body that provides information about the pipeline that is created.</p>"""
    warnings: NotRequired["capo_elastic_transcoder.types.warnings.Warnings"]
    """<p>Elastic Transcoder returns a warning if the resources used by your pipeline are not in the same region as the pipeline.</p> <p>Using resources in the same region, such as your Amazon S3 buckets, Amazon SNS notification topics, and AWS KMS key, reduces processing time and prevents cross-regional charges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePipelineResponse) -> dict:
    out: dict = {}
    if "pipeline" in value:
        import capo_elastic_transcoder.types.pipeline

        out["Pipeline"] = capo_elastic_transcoder.types.pipeline.serialize_json(
            value["pipeline"]
        )
    if "warnings" in value:
        import capo_elastic_transcoder.types.warnings

        out["Warnings"] = capo_elastic_transcoder.types.warnings.serialize_json(
            value["warnings"]
        )
    return out


def deserialize_json(data: dict) -> CreatePipelineResponse:
    out: CreatePipelineResponse = {}  # type: ignore[typeddict-item]
    if "Pipeline" in data:
        import capo_elastic_transcoder.types.pipeline

        out["pipeline"] = capo_elastic_transcoder.types.pipeline.deserialize_json(
            data["Pipeline"]
        )
    if "Warnings" in data:
        import capo_elastic_transcoder.types.warnings

        out["warnings"] = capo_elastic_transcoder.types.warnings.deserialize_json(
            data["Warnings"]
        )
    return out
