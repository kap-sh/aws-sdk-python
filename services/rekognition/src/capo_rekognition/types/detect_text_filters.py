"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectTextFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.detection_filter
    import capo_rekognition.types.regions_of_interest


class DetectTextFilters(TypedDict, closed=True):
    word_filter: NotRequired["capo_rekognition.types.detection_filter.DetectionFilter"]
    regions_of_interest: NotRequired[
        "capo_rekognition.types.regions_of_interest.RegionsOfInterest"
    ]
    """<p> A Filter focusing on a certain area of the image. Uses a <code>BoundingBox</code> object to set the region of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectTextFilters) -> dict:
    out: dict = {}
    if "word_filter" in value:
        import capo_rekognition.types.detection_filter

        out["WordFilter"] = (
            capo_rekognition.types.detection_filter.serialize_aws_json_1_1(
                value["word_filter"]
            )
        )
    if "regions_of_interest" in value:
        import capo_rekognition.types.regions_of_interest

        out["RegionsOfInterest"] = (
            capo_rekognition.types.regions_of_interest.serialize_aws_json_1_1(
                value["regions_of_interest"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectTextFilters:
    out: DetectTextFilters = {}  # type: ignore[typeddict-item]
    if "WordFilter" in data:
        import capo_rekognition.types.detection_filter

        out["word_filter"] = (
            capo_rekognition.types.detection_filter.deserialize_aws_json_1_1(
                data["WordFilter"]
            )
        )
    if "RegionsOfInterest" in data:
        import capo_rekognition.types.regions_of_interest

        out["regions_of_interest"] = (
            capo_rekognition.types.regions_of_interest.deserialize_aws_json_1_1(
                data["RegionsOfInterest"]
            )
        )
    return out
