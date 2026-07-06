"""Generated from Smithy shape ``com.amazonaws.rekognition#CelebrityDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.bounding_box
    import aws_sdk_rekognition.types.face_detail
    import aws_sdk_rekognition.types.known_gender
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.rekognition_unique_id
    import aws_sdk_rekognition.types.string
    import aws_sdk_rekognition.types.urls


class CelebrityDetail(TypedDict, closed=True):
    urls: NotRequired["aws_sdk_rekognition.types.urls.Urls"]
    """<p>An array of URLs pointing to additional celebrity information. </p>"""
    name: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The name of the celebrity.</p>"""
    id: NotRequired[
        "aws_sdk_rekognition.types.rekognition_unique_id.RekognitionUniqueId"
    ]
    """<p>The unique identifier for the celebrity. </p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The confidence, in percentage, that Amazon Rekognition has that the recognized face is the celebrity. </p>"""
    bounding_box: NotRequired["aws_sdk_rekognition.types.bounding_box.BoundingBox"]
    """<p>Bounding box around the body of a celebrity.</p>"""
    face: NotRequired["aws_sdk_rekognition.types.face_detail.FaceDetail"]
    """<p>Face details for the recognized celebrity.</p>"""
    known_gender: NotRequired["aws_sdk_rekognition.types.known_gender.KnownGender"]
    """<p>Retrieves the known gender for the celebrity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CelebrityDetail) -> dict:
    out: dict = {}
    if "urls" in value:
        import aws_sdk_rekognition.types.urls

        out["Urls"] = aws_sdk_rekognition.types.urls.serialize_aws_json_1_1(
            value["urls"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
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
    if "known_gender" in value:
        import aws_sdk_rekognition.types.known_gender

        out["KnownGender"] = (
            aws_sdk_rekognition.types.known_gender.serialize_aws_json_1_1(
                value["known_gender"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CelebrityDetail:
    out: CelebrityDetail = {}  # type: ignore[typeddict-item]
    if "Urls" in data:
        import aws_sdk_rekognition.types.urls

        out["urls"] = aws_sdk_rekognition.types.urls.deserialize_aws_json_1_1(
            data["Urls"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
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
    if "KnownGender" in data:
        import aws_sdk_rekognition.types.known_gender

        out["known_gender"] = (
            aws_sdk_rekognition.types.known_gender.deserialize_aws_json_1_1(
                data["KnownGender"]
            )
        )
    return out
