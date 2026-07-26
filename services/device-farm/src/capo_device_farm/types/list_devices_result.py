"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListDevicesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.devices
    import capo_device_farm.types.pagination_token


class ListDevicesResult(TypedDict, closed=True):
    devices: NotRequired["capo_device_farm.types.devices.Devices"]
    """<p>Information about the devices.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDevicesResult) -> dict:
    out: dict = {}
    if "devices" in value:
        import capo_device_farm.types.devices

        out["devices"] = capo_device_farm.types.devices.serialize_aws_json_1_1(
            value["devices"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDevicesResult:
    out: ListDevicesResult = {}  # type: ignore[typeddict-item]
    if "devices" in data:
        import capo_device_farm.types.devices

        out["devices"] = capo_device_farm.types.devices.deserialize_aws_json_1_1(
            data["devices"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
