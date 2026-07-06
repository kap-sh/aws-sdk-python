"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListDeviceDiscoveriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.device_discovery_list_definition
    import aws_sdk_iot_managed_integrations.types.next_token


class ListDeviceDiscoveriesResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_iot_managed_integrations.types.device_discovery_list_definition.DeviceDiscoveryListDefinition"
    ]
    """<p>The list of device discovery jobs that match the specified criteria.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token used for pagination of results when there are more device discovery jobs than can be returned in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeviceDiscoveriesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_iot_managed_integrations.types.device_discovery_list_definition

        out["Items"] = (
            aws_sdk_iot_managed_integrations.types.device_discovery_list_definition.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDeviceDiscoveriesResponse:
    out: ListDeviceDiscoveriesResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_iot_managed_integrations.types.device_discovery_list_definition

        out["items"] = (
            aws_sdk_iot_managed_integrations.types.device_discovery_list_definition.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
