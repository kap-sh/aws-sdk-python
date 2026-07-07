"""Generated from Smithy shape ``com.amazonaws.invoicing#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.resource_tag_key
    import aws_sdk_invoicing.types.resource_tag_value


class ResourceTag(TypedDict, closed=True):
    key: "aws_sdk_invoicing.types.resource_tag_key.ResourceTagKey"
    """<p>The object key of your of your resource tag. </p>"""
    value: "aws_sdk_invoicing.types.resource_tag_value.ResourceTagValue"
    """<p> The specific value of the resource tag. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("ResourceTag.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("ResourceTag.value required")
    return out
