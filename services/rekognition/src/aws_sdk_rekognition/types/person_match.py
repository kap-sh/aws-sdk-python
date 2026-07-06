"""Generated from Smithy shape ``com.amazonaws.rekognition#PersonMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_match_list
    import aws_sdk_rekognition.types.person_detail
    import aws_sdk_rekognition.types.timestamp


class PersonMatch(TypedDict, closed=True):
    timestamp: "aws_sdk_rekognition.types.timestamp.Timestamp"
    """<p>The time, in milliseconds from the beginning of the video, that the person was matched in the video.</p>"""
    person: NotRequired["aws_sdk_rekognition.types.person_detail.PersonDetail"]
    """<p>Information about the matched person.</p>"""
    face_matches: NotRequired["aws_sdk_rekognition.types.face_match_list.FaceMatchList"]
    """<p>Information about the faces in the input collection that match the face of a person in the video.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonMatch) -> dict:
    out: dict = {}
    out["Timestamp"] = value.get("timestamp", 0)
    if "person" in value:
        import aws_sdk_rekognition.types.person_detail

        out["Person"] = aws_sdk_rekognition.types.person_detail.serialize_aws_json_1_1(
            value["person"]
        )
    if "face_matches" in value:
        import aws_sdk_rekognition.types.face_match_list

        out["FaceMatches"] = (
            aws_sdk_rekognition.types.face_match_list.serialize_aws_json_1_1(
                value["face_matches"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PersonMatch:
    out: PersonMatch = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        out["timestamp"] = data["Timestamp"]
    else:
        out["timestamp"] = 0
    if "Person" in data:
        import aws_sdk_rekognition.types.person_detail

        out["person"] = (
            aws_sdk_rekognition.types.person_detail.deserialize_aws_json_1_1(
                data["Person"]
            )
        )
    if "FaceMatches" in data:
        import aws_sdk_rekognition.types.face_match_list

        out["face_matches"] = (
            aws_sdk_rekognition.types.face_match_list.deserialize_aws_json_1_1(
                data["FaceMatches"]
            )
        )
    return out
