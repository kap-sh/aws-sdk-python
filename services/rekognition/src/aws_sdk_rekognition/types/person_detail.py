"""Generated from Smithy shape ``com.amazonaws.rekognition#PersonDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.bounding_box
    import aws_sdk_rekognition.types.face_detail
    import aws_sdk_rekognition.types.person_index


class PersonDetail(TypedDict, closed=True):
    index: "aws_sdk_rekognition.types.person_index.PersonIndex"
    """<p>Identifier for the person detected person within a video. Use to keep track of the person throughout the video. The identifier is not stored by Amazon Rekognition.</p>"""
    bounding_box: NotRequired["aws_sdk_rekognition.types.bounding_box.BoundingBox"]
    """<p>Bounding box around the detected person.</p>"""
    face: NotRequired["aws_sdk_rekognition.types.face_detail.FaceDetail"]
    """<p>Face details for the detected person.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonDetail) -> dict:
    out: dict = {}
    out["Index"] = value.get("index", 0)
    if "bounding_box" in value:
        import aws_sdk_rekognition.types.bounding_box

        out["BoundingBox"] = (
            aws_sdk_rekognition.types.bounding_box.serialize_aws_json_1_1(
                value["bounding_box"]
            )
        )
    if "face" in value:
        import aws_sdk_rekognition.types.face_detail

        out["Face"] = aws_sdk_rekognition.types.face_detail.serialize_aws_json_1_1(
            value["face"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PersonDetail:
    out: PersonDetail = {}  # type: ignore[typeddict-item]
    if "Index" in data:
        out["index"] = data["Index"]
    else:
        out["index"] = 0
    if "BoundingBox" in data:
        import aws_sdk_rekognition.types.bounding_box

        out["bounding_box"] = (
            aws_sdk_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if "Face" in data:
        import aws_sdk_rekognition.types.face_detail

        out["face"] = aws_sdk_rekognition.types.face_detail.deserialize_aws_json_1_1(
            data["Face"]
        )
    return out
