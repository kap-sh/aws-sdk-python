"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.io_t_managed_integrations_resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iot_managed_integrations.types.io_t_managed_integrations_resource_arn.IoTManagedIntegrationsResourceARN"
    """<p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
