"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsearchedFace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_detail
    import aws_sdk_rekognition.types.unsearched_face_reasons


class UnsearchedFace(TypedDict, closed=True):
    face_details: NotRequired["aws_sdk_rekognition.types.face_detail.FaceDetail"]
    reasons: NotRequired[
        "aws_sdk_rekognition.types.unsearched_face_reasons.UnsearchedFaceReasons"
    ]
    """<p> Reasons why a face wasn't used for Search. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsearchedFace) -> dict:
    out: dict = {}
    if "face_details" in value:
        import aws_sdk_rekognition.types.face_detail

        out["FaceDetails"] = (
            aws_sdk_rekognition.types.face_detail.serialize_aws_json_1_1(
                value["face_details"]
            )
        )
    if "reasons" in value:
        import aws_sdk_rekognition.types.unsearched_face_reasons

        out["Reasons"] = (
            aws_sdk_rekognition.types.unsearched_face_reasons.serialize_aws_json_1_1(
                value["reasons"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsearchedFace:
    out: UnsearchedFace = {}  # type: ignore[typeddict-item]
    if "FaceDetails" in data:
        import aws_sdk_rekognition.types.face_detail

        out["face_details"] = (
            aws_sdk_rekognition.types.face_detail.deserialize_aws_json_1_1(
                data["FaceDetails"]
            )
        )
    if "Reasons" in data:
        import aws_sdk_rekognition.types.unsearched_face_reasons

        out["reasons"] = (
            aws_sdk_rekognition.types.unsearched_face_reasons.deserialize_aws_json_1_1(
                data["Reasons"]
            )
        )
    return out
