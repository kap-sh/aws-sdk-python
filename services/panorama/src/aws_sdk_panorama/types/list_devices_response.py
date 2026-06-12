"""Generated from Smithy shape ``com.amazonaws.panorama#ListDevicesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.device_list
    import aws_sdk_panorama.types.next_token


class ListDevicesResponse(TypedDict):
    devices: "aws_sdk_panorama.types.device_list.DeviceList"
    """<p>A list of devices.</p>"""
    next_token: NotRequired["aws_sdk_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesResponse) -> dict:
    out: dict = {}
    import aws_sdk_panorama.types.device_list

    out["Devices"] = aws_sdk_panorama.types.device_list.serialize_json(value["devices"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDevicesResponse:
    out: ListDevicesResponse = {}  # type: ignore[typeddict-item]
    if "Devices" in data:
        import aws_sdk_panorama.types.device_list

        out["devices"] = aws_sdk_panorama.types.device_list.deserialize_json(
            data["Devices"]
        )
    else:
        raise DeserializationError("ListDevicesResponse.devices required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
