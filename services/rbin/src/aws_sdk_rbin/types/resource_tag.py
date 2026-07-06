"""Generated from Smithy shape ``com.amazonaws.rbin#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rbin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rbin.types.resource_tag_key
    import aws_sdk_rbin.types.resource_tag_value


class ResourceTag(TypedDict, closed=True):
    resource_tag_key: "aws_sdk_rbin.types.resource_tag_key.ResourceTagKey"
    """<p>The tag key.</p>"""
    resource_tag_value: NotRequired[
        "aws_sdk_rbin.types.resource_tag_value.ResourceTagValue"
    ]
    """<p>The tag value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTag) -> dict:
    out: dict = {}
    out["ResourceTagKey"] = value["resource_tag_key"]
    if "resource_tag_value" in value:
        out["ResourceTagValue"] = value["resource_tag_value"]
    return out


def deserialize_json(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if "ResourceTagKey" in data:
        out["resource_tag_key"] = data["ResourceTagKey"]
    else:
        raise DeserializationError("ResourceTag.resource_tag_key required")
    if "ResourceTagValue" in data:
        out["resource_tag_value"] = data["ResourceTagValue"]
    return out
