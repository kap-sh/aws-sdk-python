"""Generated from Smithy shape ``com.amazonaws.emr#NotebookS3LocationForOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.uri_string
    import aws_sdk_emr.types.xml_string_max_len256


class NotebookS3LocationForOutput(TypedDict, closed=True):
    bucket: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The Amazon S3 bucket that stores the notebook execution input.</p>"""
    key: NotRequired["aws_sdk_emr.types.uri_string.UriString"]
    """<p>The key to the Amazon S3 location that stores the notebook execution input.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookS3LocationForOutput) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "key" in value:
        out["Key"] = value["key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotebookS3LocationForOutput:
    out: NotebookS3LocationForOutput = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    if "Key" in data:
        out["key"] = data["Key"]
    return out
