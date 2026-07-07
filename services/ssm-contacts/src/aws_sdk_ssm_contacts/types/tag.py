"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.tag_key
    import aws_sdk_ssm_contacts.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["aws_sdk_ssm_contacts.types.tag_key.TagKey"]
    """<p>Name of the object key.</p>"""
    value: NotRequired["aws_sdk_ssm_contacts.types.tag_value.TagValue"]
    """<p>Value of the tag.</p>"""


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
