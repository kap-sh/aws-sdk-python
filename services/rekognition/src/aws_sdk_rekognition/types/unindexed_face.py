"""Generated from Smithy shape ``com.amazonaws.rekognition#UnindexedFace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_detail
    import aws_sdk_rekognition.types.reasons


class UnindexedFace(TypedDict):
    reasons: NotRequired["aws_sdk_rekognition.types.reasons.Reasons"]
    """<p>An array of reasons that specify why a face wasn't indexed. </p> <ul> <li> <p>EXTREME_POSE - The face is at a pose that can't be detected. For example, the head is turned too far away from the camera.</p> </li> <li> <p>EXCEEDS_MAX_FACES - The number of faces detected is already higher than that specified by the <code>MaxFaces</code> input parameter for <code>IndexFaces</code>.</p> </li> <li> <p>LOW_BRIGHTNESS - The image is too dark.</p> </li> <li> <p>LOW_SHARPNESS - The image is too blurry.</p> </li> <li> <p>LOW_CONFIDENCE - The face was detected with a low confidence.</p> </li> <li> <p>SMALL_BOUNDING_BOX - The bounding box around the face is too small.</p> </li> </ul>"""
    face_detail: NotRequired["aws_sdk_rekognition.types.face_detail.FaceDetail"]
    """<p>The structure that contains attributes of a face that <code>IndexFaces</code>detected, but didn't index. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnindexedFace) -> dict:
    out: dict = {}
    if "reasons" in value:
        import aws_sdk_rekognition.types.reasons

        out["Reasons"] = aws_sdk_rekognition.types.reasons.serialize_aws_json_1_1(
            value["reasons"]
        )
    if "face_detail" in value:
        import aws_sdk_rekognition.types.face_detail

        out["FaceDetail"] = (
            aws_sdk_rekognition.types.face_detail.serialize_aws_json_1_1(
                value["face_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnindexedFace:
    out: UnindexedFace = {}  # type: ignore[typeddict-item]
    if "Reasons" in data:
        import aws_sdk_rekognition.types.reasons

        out["reasons"] = aws_sdk_rekognition.types.reasons.deserialize_aws_json_1_1(
            data["Reasons"]
        )
    if "FaceDetail" in data:
        import aws_sdk_rekognition.types.face_detail

        out["face_detail"] = (
            aws_sdk_rekognition.types.face_detail.deserialize_aws_json_1_1(
                data["FaceDetail"]
            )
        )
    return out
