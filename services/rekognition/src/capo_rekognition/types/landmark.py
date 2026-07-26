"""Generated from Smithy shape ``com.amazonaws.rekognition#Landmark``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.float
    import capo_rekognition.types.landmark_type


class Landmark(TypedDict, closed=True):
    type: NotRequired["capo_rekognition.types.landmark_type.LandmarkType"]
    """<p>Type of landmark.</p>"""
    x: NotRequired["capo_rekognition.types.float.Float"]
    """<p>The x-coordinate of the landmark expressed as a ratio of the width of the image. The x-coordinate is measured from the left-side of the image. For example, if the image is 700 pixels wide and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. </p>"""
    y: NotRequired["capo_rekognition.types.float.Float"]
    """<p>The y-coordinate of the landmark expressed as a ratio of the height of the image. The y-coordinate is measured from the top of the image. For example, if the image height is 200 pixels and the y-coordinate of the landmark is at 50 pixels, this value is 0.25.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Landmark) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_rekognition.types.landmark_type

        out["Type"] = capo_rekognition.types.landmark_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "x" in value:
        out["X"] = value["x"]
    if "y" in value:
        out["Y"] = value["y"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Landmark:
    out: Landmark = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_rekognition.types.landmark_type

        out["type"] = capo_rekognition.types.landmark_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "X" in data:
        out["x"] = data["X"]
    if "Y" in data:
        out["y"] = data["Y"]
    return out
