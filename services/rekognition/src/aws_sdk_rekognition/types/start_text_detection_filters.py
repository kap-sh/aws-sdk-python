"""Generated from Smithy shape ``com.amazonaws.rekognition#StartTextDetectionFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.detection_filter
    import aws_sdk_rekognition.types.regions_of_interest


class StartTextDetectionFilters(TypedDict):
    word_filter: NotRequired[
        "aws_sdk_rekognition.types.detection_filter.DetectionFilter"
    ]
    """<p>Filters focusing on qualities of the text, such as confidence or size.</p>"""
    regions_of_interest: NotRequired[
        "aws_sdk_rekognition.types.regions_of_interest.RegionsOfInterest"
    ]
    """<p>Filter focusing on a certain area of the frame. Uses a <code>BoundingBox</code> object to set the region of the screen.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTextDetectionFilters) -> dict:
    out: dict = {}
    if "word_filter" in value:
        import aws_sdk_rekognition.types.detection_filter

        out["WordFilter"] = (
            aws_sdk_rekognition.types.detection_filter.serialize_aws_json_1_1(
                value["word_filter"]
            )
        )
    if "regions_of_interest" in value:
        import aws_sdk_rekognition.types.regions_of_interest

        out["RegionsOfInterest"] = (
            aws_sdk_rekognition.types.regions_of_interest.serialize_aws_json_1_1(
                value["regions_of_interest"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTextDetectionFilters:
    out: StartTextDetectionFilters = {}  # type: ignore[typeddict-item]
    if "WordFilter" in data:
        import aws_sdk_rekognition.types.detection_filter

        out["word_filter"] = (
            aws_sdk_rekognition.types.detection_filter.deserialize_aws_json_1_1(
                data["WordFilter"]
            )
        )
    if "RegionsOfInterest" in data:
        import aws_sdk_rekognition.types.regions_of_interest

        out["regions_of_interest"] = (
            aws_sdk_rekognition.types.regions_of_interest.deserialize_aws_json_1_1(
                data["RegionsOfInterest"]
            )
        )
    return out
