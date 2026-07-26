"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListClientDevicesAssociatedWithCoreDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.associated_client_device_list
    import capo_greengrassv2.types.next_token_string


class ListClientDevicesAssociatedWithCoreDeviceResponse(TypedDict, closed=True):
    associated_client_devices: NotRequired[
        "capo_greengrassv2.types.associated_client_device_list.AssociatedClientDeviceList"
    ]
    """<p>A list that describes the client devices that are associated with the core device.</p>"""
    next_token: NotRequired["capo_greengrassv2.types.next_token_string.NextTokenString"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClientDevicesAssociatedWithCoreDeviceResponse) -> dict:
    out: dict = {}
    if "associated_client_devices" in value:
        import capo_greengrassv2.types.associated_client_device_list

        out["associatedClientDevices"] = (
            capo_greengrassv2.types.associated_client_device_list.serialize_json(
                value["associated_client_devices"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClientDevicesAssociatedWithCoreDeviceResponse:
    out: ListClientDevicesAssociatedWithCoreDeviceResponse = {}  # type: ignore[typeddict-item]
    if "associatedClientDevices" in data:
        import capo_greengrassv2.types.associated_client_device_list

        out["associated_client_devices"] = (
            capo_greengrassv2.types.associated_client_device_list.deserialize_json(
                data["associatedClientDevices"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
