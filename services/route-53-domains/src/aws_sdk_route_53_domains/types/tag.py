"""Generated from Smithy shape ``com.amazonaws.route53domains#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.tag_key
    import aws_sdk_route_53_domains.types.tag_value


class Tag(TypedDict):
    key: NotRequired["aws_sdk_route_53_domains.types.tag_key.TagKey"]
    """<p>The key (name) of a tag.</p> <p>Valid values: A-Z, a-z, 0-9, space, \".:/=+\-@\"</p> <p>Constraints: Each key can be 1-128 characters long.</p>"""
    value: NotRequired["aws_sdk_route_53_domains.types.tag_value.TagValue"]
    """<p>The value of a tag.</p> <p>Valid values: A-Z, a-z, 0-9, space, \".:/=+\-@\"</p> <p>Constraints: Each value can be 0-256 characters long.</p>"""


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
