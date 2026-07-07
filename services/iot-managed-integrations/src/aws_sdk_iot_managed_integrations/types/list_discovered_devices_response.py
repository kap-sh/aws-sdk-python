"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListDiscoveredDevicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.discovered_device_list_definition
    import aws_sdk_iot_managed_integrations.types.next_token


class ListDiscoveredDevicesResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_iot_managed_integrations.types.discovered_device_list_definition.DiscoveredDeviceListDefinition"
    ]
    """<p>The list of discovered devices that match the specified criteria.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token used for pagination of results when there are more discovered devices than can be returned in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDiscoveredDevicesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_iot_managed_integrations.types.discovered_device_list_definition

        out["Items"] = (
            aws_sdk_iot_managed_integrations.types.discovered_device_list_definition.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDiscoveredDevicesResponse:
    out: ListDiscoveredDevicesResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_iot_managed_integrations.types.discovered_device_list_definition

        out["items"] = (
            aws_sdk_iot_managed_integrations.types.discovered_device_list_definition.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
