"""Generated from Smithy shape ``com.amazonaws.glue#CreateJsonClassifierRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.json_path
    import aws_sdk_glue.types.name_string


class CreateJsonClassifierRequest(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    json_path: "aws_sdk_glue.types.json_path.JsonPath"
    r"""<p>A <code>JsonPath</code> string defining the JSON data for the classifier to classify. Glue supports a subset of JsonPath, as described in <a href=\"https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json\">Writing JsonPath Custom Classifiers</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateJsonClassifierRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["JsonPath"] = value["json_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateJsonClassifierRequest:
    out: CreateJsonClassifierRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateJsonClassifierRequest.name required")
    if "JsonPath" in data:
        out["json_path"] = data["JsonPath"]
    else:
        raise DeserializationError("CreateJsonClassifierRequest.json_path required")
    return out
