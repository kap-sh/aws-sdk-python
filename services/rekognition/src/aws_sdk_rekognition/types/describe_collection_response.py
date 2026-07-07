"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeCollectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.date_time
    import aws_sdk_rekognition.types.string
    import aws_sdk_rekognition.types.u_long


class DescribeCollectionResponse(TypedDict, closed=True):
    face_count: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>The number of faces that are indexed into the collection. To index faces into a collection, use <a>IndexFaces</a>.</p>"""
    face_model_version: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The version of the face model that's used by the collection for face detection.</p> <p>For more information, see Model versioning in the Amazon Rekognition Developer Guide.</p>"""
    collection_arn: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the collection.</p>"""
    creation_timestamp: NotRequired["aws_sdk_rekognition.types.date_time.DateTime"]
    """<p>The number of milliseconds since the Unix epoch time until the creation of the collection. The Unix epoch time is 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970.</p>"""
    user_count: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>The number of UserIDs assigned to the specified colleciton.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCollectionResponse) -> dict:
    out: dict = {}
    if "face_count" in value:
        out["FaceCount"] = value["face_count"]
    if "face_model_version" in value:
        out["FaceModelVersion"] = value["face_model_version"]
    if "collection_arn" in value:
        out["CollectionARN"] = value["collection_arn"]
    if "creation_timestamp" in value:
        import aws_sdk_rekognition.types.date_time

        out["CreationTimestamp"] = (
            aws_sdk_rekognition.types.date_time.serialize_aws_json_1_1(
                value["creation_timestamp"]
            )
        )
    if "user_count" in value:
        out["UserCount"] = value["user_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCollectionResponse:
    out: DescribeCollectionResponse = {}  # type: ignore[typeddict-item]
    if "FaceCount" in data:
        out["face_count"] = data["FaceCount"]
    if "FaceModelVersion" in data:
        out["face_model_version"] = data["FaceModelVersion"]
    if "CollectionARN" in data:
        out["collection_arn"] = data["CollectionARN"]
    if "CreationTimestamp" in data:
        import aws_sdk_rekognition.types.date_time

        out["creation_timestamp"] = (
            aws_sdk_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["CreationTimestamp"]
            )
        )
    if "UserCount" in data:
        out["user_count"] = data["UserCount"]
    return out
