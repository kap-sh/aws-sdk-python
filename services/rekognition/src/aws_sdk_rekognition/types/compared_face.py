"""Generated from Smithy shape ``com.amazonaws.rekognition#ComparedFace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.bounding_box
    import aws_sdk_rekognition.types.emotions
    import aws_sdk_rekognition.types.image_quality
    import aws_sdk_rekognition.types.landmarks
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.pose
    import aws_sdk_rekognition.types.smile


class ComparedFace(TypedDict, closed=True):
    bounding_box: NotRequired["aws_sdk_rekognition.types.bounding_box.BoundingBox"]
    """<p>Bounding box of the face.</p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Level of confidence that what the bounding box contains is a face.</p>"""
    landmarks: NotRequired["aws_sdk_rekognition.types.landmarks.Landmarks"]
    """<p>An array of facial landmarks.</p>"""
    pose: NotRequired["aws_sdk_rekognition.types.pose.Pose"]
    """<p>Indicates the pose of the face as determined by its pitch, roll, and yaw.</p>"""
    quality: NotRequired["aws_sdk_rekognition.types.image_quality.ImageQuality"]
    """<p>Identifies face image brightness and sharpness. </p>"""
    emotions: NotRequired["aws_sdk_rekognition.types.emotions.Emotions"]
    r"""<p> The emotions that appear to be expressed on the face, and the confidence level in the determination. Valid values include \"Happy\", \"Sad\", \"Angry\", \"Confused\", \"Disgusted\", \"Surprised\", \"Calm\", \"Unknown\", and \"Fear\". </p>"""
    smile: NotRequired["aws_sdk_rekognition.types.smile.Smile"]
    """<p> Indicates whether or not the face is smiling, and the confidence level in the determination. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComparedFace) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import aws_sdk_rekognition.types.bounding_box

        out["BoundingBox"] = (
            aws_sdk_rekognition.types.bounding_box.serialize_aws_json_1_1(
                value["bounding_box"]
            )
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "landmarks" in value:
        import aws_sdk_rekognition.types.landmarks

        out["Landmarks"] = aws_sdk_rekognition.types.landmarks.serialize_aws_json_1_1(
            value["landmarks"]
        )
    if "pose" in value:
        import aws_sdk_rekognition.types.pose

        out["Pose"] = aws_sdk_rekognition.types.pose.serialize_aws_json_1_1(
            value["pose"]
        )
    if "quality" in value:
        import aws_sdk_rekognition.types.image_quality

        out["Quality"] = aws_sdk_rekognition.types.image_quality.serialize_aws_json_1_1(
            value["quality"]
        )
    if "emotions" in value:
        import aws_sdk_rekognition.types.emotions

        out["Emotions"] = aws_sdk_rekognition.types.emotions.serialize_aws_json_1_1(
            value["emotions"]
        )
    if "smile" in value:
        import aws_sdk_rekognition.types.smile

        out["Smile"] = aws_sdk_rekognition.types.smile.serialize_aws_json_1_1(
            value["smile"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComparedFace:
    out: ComparedFace = {}  # type: ignore[typeddict-item]
    if "BoundingBox" in data:
        import aws_sdk_rekognition.types.bounding_box

        out["bounding_box"] = (
            aws_sdk_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Landmarks" in data:
        import aws_sdk_rekognition.types.landmarks

        out["landmarks"] = aws_sdk_rekognition.types.landmarks.deserialize_aws_json_1_1(
            data["Landmarks"]
        )
    if "Pose" in data:
        import aws_sdk_rekognition.types.pose

        out["pose"] = aws_sdk_rekognition.types.pose.deserialize_aws_json_1_1(
            data["Pose"]
        )
    if "Quality" in data:
        import aws_sdk_rekognition.types.image_quality

        out["quality"] = (
            aws_sdk_rekognition.types.image_quality.deserialize_aws_json_1_1(
                data["Quality"]
            )
        )
    if "Emotions" in data:
        import aws_sdk_rekognition.types.emotions

        out["emotions"] = aws_sdk_rekognition.types.emotions.deserialize_aws_json_1_1(
            data["Emotions"]
        )
    if "Smile" in data:
        import aws_sdk_rekognition.types.smile

        out["smile"] = aws_sdk_rekognition.types.smile.deserialize_aws_json_1_1(
            data["Smile"]
        )
    return out
