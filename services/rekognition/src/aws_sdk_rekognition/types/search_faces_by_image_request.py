"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchFacesByImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.collection_id
    import aws_sdk_rekognition.types.image
    import aws_sdk_rekognition.types.max_faces
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.quality_filter


class SearchFacesByImageRequest(TypedDict, closed=True):
    collection_id: "aws_sdk_rekognition.types.collection_id.CollectionId"
    """<p>ID of the collection to search.</p>"""
    image: "aws_sdk_rekognition.types.image.Image"
    """<p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>"""
    max_faces: NotRequired["aws_sdk_rekognition.types.max_faces.MaxFaces"]
    """<p>Maximum number of faces to return. The operation returns the maximum number of faces with the highest confidence in the match.</p>"""
    face_match_threshold: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>(Optional) Specifies the minimum confidence in the face match to return. For example, don't return any matches where confidence in matches is less than 70%. The default value is 80%.</p>"""
    quality_filter: NotRequired[
        "aws_sdk_rekognition.types.quality_filter.QualityFilter"
    ]
    """<p>A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren't searched for in the collection. If you specify <code>AUTO</code>, Amazon Rekognition chooses the quality bar. If you specify <code>LOW</code>, <code>MEDIUM</code>, or <code>HIGH</code>, filtering removes all faces that don’t meet the chosen quality bar. The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object that's misidentified as a face, a face that's too blurry, or a face with a pose that's too extreme to use. If you specify <code>NONE</code>, no filtering is performed. The default value is <code>NONE</code>. </p> <p>To use quality filtering, the collection you are using must be associated with version 3 of the face model or higher.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFacesByImageRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    import aws_sdk_rekognition.types.image

    out["Image"] = aws_sdk_rekognition.types.image.serialize_aws_json_1_1(
        value["image"]
    )
    if "max_faces" in value:
        out["MaxFaces"] = value["max_faces"]
    if "face_match_threshold" in value:
        out["FaceMatchThreshold"] = value["face_match_threshold"]
    if "quality_filter" in value:
        import aws_sdk_rekognition.types.quality_filter

        out["QualityFilter"] = (
            aws_sdk_rekognition.types.quality_filter.serialize_aws_json_1_1(
                value["quality_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchFacesByImageRequest:
    out: SearchFacesByImageRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("SearchFacesByImageRequest.collection_id required")
    if "Image" in data:
        import aws_sdk_rekognition.types.image

        out["image"] = aws_sdk_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("SearchFacesByImageRequest.image required")
    if "MaxFaces" in data:
        out["max_faces"] = data["MaxFaces"]
    if "FaceMatchThreshold" in data:
        out["face_match_threshold"] = data["FaceMatchThreshold"]
    if "QualityFilter" in data:
        import aws_sdk_rekognition.types.quality_filter

        out["quality_filter"] = (
            aws_sdk_rekognition.types.quality_filter.deserialize_aws_json_1_1(
                data["QualityFilter"]
            )
        )
    return out
