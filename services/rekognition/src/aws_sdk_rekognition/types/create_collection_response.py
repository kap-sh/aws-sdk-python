"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateCollectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.string
    import aws_sdk_rekognition.types.u_integer


class CreateCollectionResponse(TypedDict):
    status_code: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p>HTTP status code indicating the result of the operation.</p>"""
    collection_arn: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the collection. You can use this to manage permissions on your resources. </p>"""
    face_model_version: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>Version number of the face detection model associated with the collection you are creating.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCollectionResponse) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["StatusCode"] = value["status_code"]
    if "collection_arn" in value:
        out["CollectionArn"] = value["collection_arn"]
    if "face_model_version" in value:
        out["FaceModelVersion"] = value["face_model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCollectionResponse:
    out: CreateCollectionResponse = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        out["status_code"] = data["StatusCode"]
    if "CollectionArn" in data:
        out["collection_arn"] = data["CollectionArn"]
    if "FaceModelVersion" in data:
        out["face_model_version"] = data["FaceModelVersion"]
    return out
