"""Generated from Smithy shape ``com.amazonaws.glue#UpdateJsonClassifierRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.json_path
    import aws_sdk_glue.types.name_string


class UpdateJsonClassifierRequest(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    json_path: NotRequired["aws_sdk_glue.types.json_path.JsonPath"]
    r"""<p>A <code>JsonPath</code> string defining the JSON data for the classifier to classify. Glue supports a subset of JsonPath, as described in <a href=\"https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json\">Writing JsonPath Custom Classifiers</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateJsonClassifierRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "json_path" in value:
        out["JsonPath"] = value["json_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateJsonClassifierRequest:
    out: UpdateJsonClassifierRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateJsonClassifierRequest.name required")
    if "JsonPath" in data:
        out["json_path"] = data["JsonPath"]
    return out
