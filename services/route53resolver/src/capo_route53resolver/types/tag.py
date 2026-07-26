"""Generated from Smithy shape ``com.amazonaws.route53resolver#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.tag_key
    import capo_route53resolver.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_route53resolver.types.tag_key.TagKey"
    """<p>The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of <code>Key</code> might be <code>account-id</code>.</p>"""
    value: "capo_route53resolver.types.tag_value.TagValue"
    """<p>The value for the tag. For example, if <code>Key</code> is <code>account-id</code>, then <code>Value</code> might be the ID of the customer account that you're creating the resource for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("Tag.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Tag.value required")
    return out
