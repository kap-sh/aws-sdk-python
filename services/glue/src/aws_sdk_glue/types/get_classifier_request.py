"""Generated from Smithy shape ``com.amazonaws.glue#GetClassifierRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class GetClassifierRequest(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Name of the classifier to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetClassifierRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetClassifierRequest:
    out: GetClassifierRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetClassifierRequest.name required")
    return out
