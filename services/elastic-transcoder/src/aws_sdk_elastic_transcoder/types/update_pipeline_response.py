"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#UpdatePipelineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.pipeline
    import aws_sdk_elastic_transcoder.types.warnings


class UpdatePipelineResponse(TypedDict, closed=True):
    pipeline: NotRequired["aws_sdk_elastic_transcoder.types.pipeline.Pipeline"]
    """<p>The pipeline updated by this <code>UpdatePipelineResponse</code> call.</p>"""
    warnings: NotRequired["aws_sdk_elastic_transcoder.types.warnings.Warnings"]
    """<p>Elastic Transcoder returns a warning if the resources used by your pipeline are not in the same region as the pipeline.</p> <p>Using resources in the same region, such as your Amazon S3 buckets, Amazon SNS notification topics, and AWS KMS key, reduces processing time and prevents cross-regional charges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePipelineResponse) -> dict:
    out: dict = {}
    if "pipeline" in value:
        import aws_sdk_elastic_transcoder.types.pipeline

        out["Pipeline"] = aws_sdk_elastic_transcoder.types.pipeline.serialize_json(
            value["pipeline"]
        )
    if "warnings" in value:
        import aws_sdk_elastic_transcoder.types.warnings

        out["Warnings"] = aws_sdk_elastic_transcoder.types.warnings.serialize_json(
            value["warnings"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePipelineResponse:
    out: UpdatePipelineResponse = {}  # type: ignore[typeddict-item]
    if "Pipeline" in data:
        import aws_sdk_elastic_transcoder.types.pipeline

        out["pipeline"] = aws_sdk_elastic_transcoder.types.pipeline.deserialize_json(
            data["Pipeline"]
        )
    if "Warnings" in data:
        import aws_sdk_elastic_transcoder.types.warnings

        out["warnings"] = aws_sdk_elastic_transcoder.types.warnings.deserialize_json(
            data["Warnings"]
        )
    return out
