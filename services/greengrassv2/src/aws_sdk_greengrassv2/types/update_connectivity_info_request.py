"""Generated from Smithy shape ``com.amazonaws.greengrassv2#UpdateConnectivityInfoRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.connectivity_info_list
    import aws_sdk_greengrassv2.types.core_device_thing_name


class UpdateConnectivityInfoRequest(TypedDict):
    thing_name: "aws_sdk_greengrassv2.types.core_device_thing_name.CoreDeviceThingName"
    """<p>The name of the core device. This is also the name of the IoT thing.</p>"""
    connectivity_info: (
        "aws_sdk_greengrassv2.types.connectivity_info_list.connectivityInfoList"
    )
    """<p>The connectivity information for the core device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectivityInfoRequest) -> dict:
    out: dict = {}
    import aws_sdk_greengrassv2.types.connectivity_info_list

    out["ConnectivityInfo"] = (
        aws_sdk_greengrassv2.types.connectivity_info_list.serialize_json(
            value["connectivity_info"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConnectivityInfoRequest:
    out: UpdateConnectivityInfoRequest = {}  # type: ignore[typeddict-item]
    if "ConnectivityInfo" in data:
        import aws_sdk_greengrassv2.types.connectivity_info_list

        out["connectivity_info"] = (
            aws_sdk_greengrassv2.types.connectivity_info_list.deserialize_json(
                data["ConnectivityInfo"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConnectivityInfoRequest.connectivity_info required"
        )
    return out
