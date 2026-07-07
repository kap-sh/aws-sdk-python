"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImagePipelineAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_pipeline_arn
    import aws_sdk_imagebuilder.types.severity_counts


class ImagePipelineAggregation(TypedDict, closed=True):
    image_pipeline_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the image pipeline for this aggregation.</p>"""
    severity_counts: NotRequired[
        "aws_sdk_imagebuilder.types.severity_counts.SeverityCounts"
    ]
    """<p>Counts by severity level for medium severity and higher level findings, plus a total for all of the findings for the specified image pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImagePipelineAggregation) -> dict:
    out: dict = {}
    if "image_pipeline_arn" in value:
        out["imagePipelineArn"] = value["image_pipeline_arn"]
    if "severity_counts" in value:
        import aws_sdk_imagebuilder.types.severity_counts

        out["severityCounts"] = (
            aws_sdk_imagebuilder.types.severity_counts.serialize_json(
                value["severity_counts"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImagePipelineAggregation:
    out: ImagePipelineAggregation = {}  # type: ignore[typeddict-item]
    if "imagePipelineArn" in data:
        out["image_pipeline_arn"] = data["imagePipelineArn"]
    if "severityCounts" in data:
        import aws_sdk_imagebuilder.types.severity_counts

        out["severity_counts"] = (
            aws_sdk_imagebuilder.types.severity_counts.deserialize_json(
                data["severityCounts"]
            )
        )
    return out
