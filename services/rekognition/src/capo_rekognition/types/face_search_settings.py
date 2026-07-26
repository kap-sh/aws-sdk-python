"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceSearchSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.percent


class FaceSearchSettings(TypedDict, closed=True):
    collection_id: NotRequired["capo_rekognition.types.collection_id.CollectionId"]
    """<p>The ID of a collection that contains faces that you want to search for.</p>"""
    face_match_threshold: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Minimum face match confidence score that must be met to return a result for a recognized face. The default is 80. 0 is the lowest confidence. 100 is the highest confidence. Values between 0 and 100 are accepted, and values lower than 80 are set to 80.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceSearchSettings) -> dict:
    out: dict = {}
    if "collection_id" in value:
        out["CollectionId"] = value["collection_id"]
    if "face_match_threshold" in value:
        out["FaceMatchThreshold"] = value["face_match_threshold"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FaceSearchSettings:
    out: FaceSearchSettings = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    if "FaceMatchThreshold" in data:
        out["face_match_threshold"] = data["FaceMatchThreshold"]
    return out
