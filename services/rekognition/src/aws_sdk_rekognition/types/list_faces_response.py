"""Generated from Smithy shape ``com.amazonaws.rekognition#ListFacesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_list
    import aws_sdk_rekognition.types.string


class ListFacesResponse(TypedDict):
    faces: NotRequired["aws_sdk_rekognition.types.face_list.FaceList"]
    """<p>An array of <code>Face</code> objects. </p>"""
    next_token: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>If the response is truncated, Amazon Rekognition returns this token that you can use in the subsequent request to retrieve the next set of faces.</p>"""
    face_model_version: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>Version number of the face detection model associated with the input collection (<code>CollectionId</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFacesResponse) -> dict:
    out: dict = {}
    if "faces" in value:
        import aws_sdk_rekognition.types.face_list

        out["Faces"] = aws_sdk_rekognition.types.face_list.serialize_aws_json_1_1(
            value["faces"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "face_model_version" in value:
        out["FaceModelVersion"] = value["face_model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFacesResponse:
    out: ListFacesResponse = {}  # type: ignore[typeddict-item]
    if "Faces" in data:
        import aws_sdk_rekognition.types.face_list

        out["faces"] = aws_sdk_rekognition.types.face_list.deserialize_aws_json_1_1(
            data["Faces"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "FaceModelVersion" in data:
        out["face_model_version"] = data["FaceModelVersion"]
    return out
