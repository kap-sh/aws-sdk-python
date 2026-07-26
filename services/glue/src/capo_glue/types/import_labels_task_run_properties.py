"""Generated from Smithy shape ``com.amazonaws.glue#ImportLabelsTaskRunProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.replace_boolean
    import capo_glue.types.uri_string


class ImportLabelsTaskRunProperties(TypedDict, closed=True):
    input_s3_path: NotRequired["capo_glue.types.uri_string.UriString"]
    """<p>The Amazon Simple Storage Service (Amazon S3) path from where you will import the labels.</p>"""
    replace: "capo_glue.types.replace_boolean.ReplaceBoolean"
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
