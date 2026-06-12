"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListCoreDevicesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.core_devices_list
    import aws_sdk_greengrassv2.types.next_token_string


class ListCoreDevicesResponse(TypedDict):
    core_devices: NotRequired[
        "aws_sdk_greengrassv2.types.core_devices_list.CoreDevicesList"
    ]
    """<p>A list that summarizes each core device.</p>"""
    next_token: NotRequired[
        "aws_sdk_greengrassv2.types.next_token_string.NextTokenString"
    ]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreDevicesResponse) -> dict:
    out: dict = {}
    if "core_devices" in value:
        import aws_sdk_greengrassv2.types.core_devices_list

        out["coreDevices"] = (
            aws_sdk_greengrassv2.types.core_devices_list.serialize_json(
                value["core_devices"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCoreDevicesResponse:
    out: ListCoreDevicesResponse = {}  # type: ignore[typeddict-item]
    if "coreDevices" in data:
        import aws_sdk_greengrassv2.types.core_devices_list

        out["core_devices"] = (
            aws_sdk_greengrassv2.types.core_devices_list.deserialize_json(
                data["coreDevices"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
