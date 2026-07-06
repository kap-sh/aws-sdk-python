"""Generated from Smithy shape ``com.amazonaws.billing#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.resource_tag_key
    import aws_sdk_billing.types.resource_tag_value


class ResourceTag(TypedDict, closed=True):
    key: "aws_sdk_billing.types.resource_tag_key.ResourceTagKey"
    """<p> The key that's associated with the tag. </p>"""
    value: NotRequired["aws_sdk_billing.types.resource_tag_value.ResourceTagValue"]
    """<p> The value that's associated with the tag. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ResourceTag.key required")
    if "value" in data:
        out["value"] = data["value"]
    return out
