"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.amazon_resource_name
    import capo_iotdeviceadvisor.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    """<p>The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.</p>"""
    tags: NotRequired["capo_iotdeviceadvisor.types.tag_map.TagMap"]
    """<p>The tags to be attached to the IoT Device Advisor resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_iotdeviceadvisor.types.tag_map

        out["tags"] = capo_iotdeviceadvisor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_iotdeviceadvisor.types.tag_map

        out["tags"] = capo_iotdeviceadvisor.types.tag_map.deserialize_json(data["tags"])
    return out
