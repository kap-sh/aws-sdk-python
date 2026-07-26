"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchFacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.face_id
    import capo_rekognition.types.max_faces
    import capo_rekognition.types.percent


class SearchFacesRequest(TypedDict, closed=True):
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>ID of the collection the face belongs to.</p>"""
    face_id: "capo_rekognition.types.face_id.FaceId"
    """<p>ID of a face to find matches for in the collection.</p>"""
    max_faces: NotRequired["capo_rekognition.types.max_faces.MaxFaces"]
    """<p>Maximum number of faces to return. The operation returns the maximum number of faces with the highest confidence in the match.</p>"""
    face_match_threshold: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Optional value specifying the minimum confidence in the face match to return. For example, don't return any matches where confidence in matches is less than 70%. The default value is 80%. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFacesRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    out["FaceId"] = value["face_id"]
    if "max_faces" in value:
        out["MaxFaces"] = value["max_faces"]
    if "face_match_threshold" in value:
        out["FaceMatchThreshold"] = value["face_match_threshold"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchFacesRequest:
    out: SearchFacesRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("SearchFacesRequest.collection_id required")
    if "FaceId" in data:
        out["face_id"] = data["FaceId"]
    else:
        raise DeserializationError("SearchFacesRequest.face_id required")
    if "MaxFaces" in data:
        out["max_faces"] = data["MaxFaces"]
    if "FaceMatchThreshold" in data:
        out["face_match_threshold"] = data["FaceMatchThreshold"]
    return out
