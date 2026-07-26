"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.resource_tag_key
    import capo_bcm_data_exports.types.resource_tag_value


class ResourceTag(TypedDict, closed=True):
    key: "capo_bcm_data_exports.types.resource_tag_key.ResourceTagKey"
    """<p>The key that's associated with the tag.</p>"""
    value: "capo_bcm_data_exports.types.resource_tag_value.ResourceTagValue"
    """<p>The value that's associated with the tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceTag:
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
