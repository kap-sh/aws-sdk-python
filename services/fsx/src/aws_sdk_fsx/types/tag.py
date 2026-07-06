"""Generated from Smithy shape ``com.amazonaws.fsx#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.tag_key
    import aws_sdk_fsx.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["aws_sdk_fsx.types.tag_key.TagKey"]
    """<p>A value that specifies the <code>TagKey</code>, the name of the tag. Tag keys must be unique for the resource to which they are attached.</p>"""
    value: NotRequired["aws_sdk_fsx.types.tag_value.TagValue"]
    """<p>A value that specifies the <code>TagValue</code>, the value assigned to the corresponding tag key. Tag values can be null and don't have to be unique in a tag set. For example, you can have a key-value pair in a tag set of <code>finances : April</code> and also of <code>payroll : April</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
