"""Generated from Smithy shape ``com.amazonaws.glue#S3DirectSourceAdditionalOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.boxed_long
    import capo_glue.types.enclosed_in_string_property


class S3DirectSourceAdditionalOptions(TypedDict, closed=True):
    bounded_size: NotRequired["capo_glue.types.boxed_long.BoxedLong"]
    """<p>Sets the upper limit for the target size of the dataset in bytes that will be processed.</p>"""
    bounded_files: NotRequired["capo_glue.types.boxed_long.BoxedLong"]
    """<p>Sets the upper limit for the target number of files that will be processed.</p>"""
    enable_sample_path: NotRequired["capo_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Sets option to enable a sample path.</p>"""
    sample_path: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>If enabled, specifies the sample path.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DirectSourceAdditionalOptions) -> dict:
    out: dict = {}
    if "bounded_size" in value:
        out["BoundedSize"] = value["bounded_size"]
    if "bounded_files" in value:
        out["BoundedFiles"] = value["bounded_files"]
    if "enable_sample_path" in value:
        out["EnableSamplePath"] = value["enable_sample_path"]
    if "sample_path" in value:
        out["SamplePath"] = value["sample_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DirectSourceAdditionalOptions:
    out: S3DirectSourceAdditionalOptions = {}  # type: ignore[typeddict-item]
    if "BoundedSize" in data:
        out["bounded_size"] = data["BoundedSize"]
    if "BoundedFiles" in data:
        out["bounded_files"] = data["BoundedFiles"]
    if "EnableSamplePath" in data:
        out["enable_sample_path"] = data["EnableSamplePath"]
    if "SamplePath" in data:
        out["sample_path"] = data["SamplePath"]
    return out
