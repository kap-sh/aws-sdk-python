"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.amazon_resource_name
    import capo_iotdeviceadvisor.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    """<p>The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.</p>"""
    tag_keys: NotRequired["capo_iotdeviceadvisor.types.tag_key_list.TagKeyList"]
    """<p>List of tag keys to remove from the IoT Device Advisor resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
