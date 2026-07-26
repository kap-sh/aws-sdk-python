"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_build_version_arn
    import capo_imagebuilder.types.severity_counts


class ImageAggregation(TypedDict, closed=True):
    image_build_version_arn: NotRequired[
        "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the image for this aggregation.</p>"""
    severity_counts: NotRequired[
        "capo_imagebuilder.types.severity_counts.SeverityCounts"
    ]
    """<p>Counts by severity level for medium severity and higher level findings, plus a total for all of the findings for the specified image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageAggregation) -> dict:
    out: dict = {}
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    if "severity_counts" in value:
        import capo_imagebuilder.types.severity_counts

        out["severityCounts"] = capo_imagebuilder.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    return out


def deserialize_json(data: dict) -> ImageAggregation:
    out: ImageAggregation = {}  # type: ignore[typeddict-item]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    if "severityCounts" in data:
        import capo_imagebuilder.types.severity_counts

        out["severity_counts"] = (
            capo_imagebuilder.types.severity_counts.deserialize_json(
                data["severityCounts"]
            )
        )
    return out
