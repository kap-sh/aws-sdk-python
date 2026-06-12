"""Generated from Smithy shape ``com.amazonaws.glue#ImportLabelsTaskRunProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.replace_boolean
    import aws_sdk_glue.types.uri_string


class ImportLabelsTaskRunProperties(TypedDict):
    input_s3_path: NotRequired["aws_sdk_glue.types.uri_string.UriString"]
    """<p>The Amazon Simple Storage Service (Amazon S3) path from where you will import the labels.</p>"""
    replace: "aws_sdk_glue.types.replace_boolean.ReplaceBoolean"
    """<p>Indicates whether to overwrite your existing labels.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportLabelsTaskRunProperties) -> dict:
    out: dict = {}
    if "input_s3_path" in value:
        out["InputS3Path"] = value["input_s3_path"]
    out["Replace"] = value.get("replace", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportLabelsTaskRunProperties:
    out: ImportLabelsTaskRunProperties = {}  # type: ignore[typeddict-item]
    if "InputS3Path" in data:
        out["input_s3_path"] = data["InputS3Path"]
    if "Replace" in data:
        out["replace"] = data["Replace"]
    else:
        out["replace"] = False
    return out
