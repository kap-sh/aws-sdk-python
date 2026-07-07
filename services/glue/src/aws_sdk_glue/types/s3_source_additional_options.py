"""Generated from Smithy shape ``com.amazonaws.glue#S3SourceAdditionalOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.boxed_long


class S3SourceAdditionalOptions(TypedDict, closed=True):
    bounded_size: NotRequired["aws_sdk_glue.types.boxed_long.BoxedLong"]
    """<p>Sets the upper limit for the target size of the dataset in bytes that will be processed.</p>"""
    bounded_files: NotRequired["aws_sdk_glue.types.boxed_long.BoxedLong"]
    """<p>Sets the upper limit for the target number of files that will be processed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3SourceAdditionalOptions) -> dict:
    out: dict = {}
    if "bounded_size" in value:
        out["BoundedSize"] = value["bounded_size"]
    if "bounded_files" in value:
        out["BoundedFiles"] = value["bounded_files"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3SourceAdditionalOptions:
    out: S3SourceAdditionalOptions = {}  # type: ignore[typeddict-item]
    if "BoundedSize" in data:
        out["bounded_size"] = data["BoundedSize"]
    if "BoundedFiles" in data:
        out["bounded_files"] = data["BoundedFiles"]
    return out
