"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#DetectEntitiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.bounded_length_string


class DetectEntitiesRequest(TypedDict):
    text: "aws_sdk_comprehendmedical.types.bounded_length_string.BoundedLengthString"
    """<p> A UTF-8 text string containing the clinical content being examined for entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectEntitiesRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectEntitiesRequest:
    out: DetectEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("DetectEntitiesRequest.text required")
    return out
