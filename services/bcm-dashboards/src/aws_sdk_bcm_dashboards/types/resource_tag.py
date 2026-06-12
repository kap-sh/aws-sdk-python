"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ResourceTag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.resource_tag_key
    import aws_sdk_bcm_dashboards.types.resource_tag_value


class ResourceTag(TypedDict):
    key: "aws_sdk_bcm_dashboards.types.resource_tag_key.ResourceTagKey"
    """<p>The key of the tag to be attached to the dashboard resource.</p>"""
    value: "aws_sdk_bcm_dashboards.types.resource_tag_value.ResourceTagValue"
    """<p>The value of the tag to be attached to the dashboard resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
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
    else:
        raise DeserializationError("ResourceTag.value required")
    return out
