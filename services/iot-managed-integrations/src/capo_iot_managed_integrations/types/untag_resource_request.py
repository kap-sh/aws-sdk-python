"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.io_t_managed_integrations_resource_arn
    import capo_iot_managed_integrations.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iot_managed_integrations.types.io_t_managed_integrations_resource_arn.IoTManagedIntegrationsResourceARN"
    """<p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>"""
    tag_keys: "capo_iot_managed_integrations.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
