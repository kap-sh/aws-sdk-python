"""Generated from Smithy shape ``com.amazonaws.rekognition#Celebrity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.compared_face
    import capo_rekognition.types.known_gender
    import capo_rekognition.types.percent
    import capo_rekognition.types.rekognition_unique_id
    import capo_rekognition.types.string
    import capo_rekognition.types.urls


class Celebrity(TypedDict, closed=True):
    urls: NotRequired["capo_rekognition.types.urls.Urls"]
    """<p>An array of URLs pointing to additional information about the celebrity. If there is no additional information about the celebrity, this list is empty.</p>"""
    name: NotRequired["capo_rekognition.types.string.String"]
    """<p>The name of the celebrity.</p>"""
    id: NotRequired["capo_rekognition.types.rekognition_unique_id.RekognitionUniqueId"]
    """<p>A unique identifier for the celebrity. </p>"""
    face: NotRequired["capo_rekognition.types.compared_face.ComparedFace"]
    """<p>Provides information about the celebrity's face, such as its location on the image.</p>"""
    match_confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>The confidence, in percentage, that Amazon Rekognition has that the recognized face is the celebrity.</p>"""
    known_gender: NotRequired["capo_rekognition.types.known_gender.KnownGender"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Celebrity) -> dict:
    out: dict = {}
    if "urls" in value:
        import capo_rekognition.types.urls

        out["Urls"] = capo_rekognition.types.urls.serialize_aws_json_1_1(value["urls"])
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "face" in value:
        import capo_rekognition.types.compared_face

        out["Face"] = capo_rekognition.types.compared_face.serialize_aws_json_1_1(
            value["face"]
        )
    if "match_confidence" in value:
        out["MatchConfidence"] = value["match_confidence"]
    if "known_gender" in value:
        import capo_rekognition.types.known_gender

        out["KnownGender"] = capo_rekognition.types.known_gender.serialize_aws_json_1_1(
            value["known_gender"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Celebrity:
    out: Celebrity = {}  # type: ignore[typeddict-item]
    if "Urls" in data:
        import capo_rekognition.types.urls

        out["urls"] = capo_rekognition.types.urls.deserialize_aws_json_1_1(data["Urls"])
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Face" in data:
        import capo_rekognition.types.compared_face

        out["face"] = capo_rekognition.types.compared_face.deserialize_aws_json_1_1(
            data["Face"]
        )
    if "MatchConfidence" in data:
        out["match_confidence"] = data["MatchConfidence"]
    if "KnownGender" in data:
        import capo_rekognition.types.known_gender

        out["known_gender"] = (
            capo_rekognition.types.known_gender.deserialize_aws_json_1_1(
                data["KnownGender"]
            )
        )
    return out
