"""Generated from Smithy shape ``com.amazonaws.rekognition#GetCelebrityInfoRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.rekognition_unique_id


class GetCelebrityInfoRequest(TypedDict, closed=True):
    id: "capo_rekognition.types.rekognition_unique_id.RekognitionUniqueId"
    """<p>The ID for the celebrity. You get the celebrity ID from a call to the <a>RecognizeCelebrities</a> operation, which recognizes celebrities in an image. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCelebrityInfoRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCelebrityInfoRequest:
    out: GetCelebrityInfoRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("GetCelebrityInfoRequest.id required")
    return out
