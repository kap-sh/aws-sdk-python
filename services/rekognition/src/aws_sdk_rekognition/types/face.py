"""Generated from Smithy shape ``com.amazonaws.rekognition#Face``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.bounding_box
    import aws_sdk_rekognition.types.external_image_id
    import aws_sdk_rekognition.types.face_id
    import aws_sdk_rekognition.types.image_id
    import aws_sdk_rekognition.types.index_faces_model_version
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.user_id


class Face(TypedDict):
    face_id: NotRequired["aws_sdk_rekognition.types.face_id.FaceId"]
    """<p>Unique identifier that Amazon Rekognition assigns to the face.</p>"""
    bounding_box: NotRequired["aws_sdk_rekognition.types.bounding_box.BoundingBox"]
    """<p>Bounding box of the face.</p>"""
    image_id: NotRequired["aws_sdk_rekognition.types.image_id.ImageId"]
    """<p>Unique identifier that Amazon Rekognition assigns to the input image.</p>"""
    external_image_id: NotRequired[
        "aws_sdk_rekognition.types.external_image_id.ExternalImageId"
    ]
    """<p>Identifier that you assign to all the faces in the input image.</p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Confidence level that the bounding box contains a face (and not a different object such as a tree).</p>"""
    index_faces_model_version: NotRequired[
        "aws_sdk_rekognition.types.index_faces_model_version.IndexFacesModelVersion"
    ]
    """<p> The version of the face detect and storage model that was used when indexing the face vector. </p>"""
    user_id: NotRequired["aws_sdk_rekognition.types.user_id.UserId"]
    """<p>Unique identifier assigned to the user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Face) -> dict:
    out: dict = {}
    if "face_id" in value:
        out["FaceId"] = value["face_id"]
    if "bounding_box" in value:
        import aws_sdk_rekognition.types.bounding_box

        out["BoundingBox"] = (
            aws_sdk_rekognition.types.bounding_box.serialize_aws_json_1_1(
                value["bounding_box"]
            )
        )
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "external_image_id" in value:
        out["ExternalImageId"] = value["external_image_id"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "index_faces_model_version" in value:
        out["IndexFacesModelVersion"] = value["index_faces_model_version"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Face:
    out: Face = {}  # type: ignore[typeddict-item]
    if "FaceId" in data:
        out["face_id"] = data["FaceId"]
    if "BoundingBox" in data:
        import aws_sdk_rekognition.types.bounding_box

        out["bounding_box"] = (
            aws_sdk_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    if "ExternalImageId" in data:
        out["external_image_id"] = data["ExternalImageId"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "IndexFacesModelVersion" in data:
        out["index_faces_model_version"] = data["IndexFacesModelVersion"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    return out
