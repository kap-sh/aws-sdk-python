"""Generated from Smithy shape ``com.amazonaws.rekognition#RegionOfInterest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.bounding_box
    import capo_rekognition.types.polygon


class RegionOfInterest(TypedDict, closed=True):
    bounding_box: NotRequired["capo_rekognition.types.bounding_box.BoundingBox"]
    """<p>The box representing a region of interest on screen.</p>"""
    polygon: NotRequired["capo_rekognition.types.polygon.Polygon"]
    """<p> Specifies a shape made up of up to 10 <code>Point</code> objects to define a region of interest. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionOfInterest) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_rekognition.types.bounding_box

        out["BoundingBox"] = capo_rekognition.types.bounding_box.serialize_aws_json_1_1(
            value["bounding_box"]
        )
    if "polygon" in value:
        import capo_rekognition.types.polygon

        out["Polygon"] = capo_rekognition.types.polygon.serialize_aws_json_1_1(
            value["polygon"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionOfInterest:
    out: RegionOfInterest = {}  # type: ignore[typeddict-item]
    if "BoundingBox" in data:
        import capo_rekognition.types.bounding_box

        out["bounding_box"] = (
            capo_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if "Polygon" in data:
        import capo_rekognition.types.polygon

        out["polygon"] = capo_rekognition.types.polygon.deserialize_aws_json_1_1(
            data["Polygon"]
        )
    return out
