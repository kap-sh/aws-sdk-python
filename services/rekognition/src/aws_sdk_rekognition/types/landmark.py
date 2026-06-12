"""Generated from Smithy shape ``com.amazonaws.rekognition#Landmark``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.float
    import aws_sdk_rekognition.types.landmark_type


class Landmark(TypedDict):
    type: NotRequired["aws_sdk_rekognition.types.landmark_type.LandmarkType"]
    """<p>Type of landmark.</p>"""
    x: NotRequired["aws_sdk_rekognition.types.float.Float"]
    """<p>The x-coordinate of the landmark expressed as a ratio of the width of the image. The x-coordinate is measured from the left-side of the image. For example, if the image is 700 pixels wide and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. </p>"""
    y: NotRequired["aws_sdk_rekognition.types.float.Float"]
    """<p>The y-coordinate of the landmark expressed as a ratio of the height of the image. The y-coordinate is measured from the top of the image. For example, if the image height is 200 pixels and the y-coordinate of the landmark is at 50 pixels, this value is 0.25.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Landmark) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_rekognition.types.landmark_type

        out["Type"] = aws_sdk_rekognition.types.landmark_type.serialize_aws_json_1_1(
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
        import aws_sdk_rekognition.types.landmark_type

        out["type"] = aws_sdk_rekognition.types.landmark_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "X" in data:
        out["x"] = data["X"]
    if "Y" in data:
        out["y"] = data["Y"]
    return out
