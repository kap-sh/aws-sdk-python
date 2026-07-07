"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListDeviceDiscoveriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.device_discovery_status
    import aws_sdk_iot_managed_integrations.types.discovery_type
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token


class ListDeviceDiscoveriesRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token used for pagination of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of device discovery jobs to return in a single response.</p>"""
    type_filter: NotRequired[
        "aws_sdk_iot_managed_integrations.types.discovery_type.DiscoveryType"
    ]
    """<p>The discovery type to filter device discovery jobs by.</p>"""
    status_filter: NotRequired[
        "aws_sdk_iot_managed_integrations.types.device_discovery_status.DeviceDiscoveryStatus"
    ]
    """<p>The status to filter device discovery jobs by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeviceDiscoveriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDeviceDiscoveriesRequest:
    out: ListDeviceDiscoveriesRequest = {}  # type: ignore[typeddict-item]
    return out
