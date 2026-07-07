"""Generated from Smithy shape ``com.amazonaws.location#VerifyDevicePositionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.device_state
    import aws_sdk_location.types.distance_unit
    import aws_sdk_location.types.resource_name


class VerifyDevicePositionRequest(TypedDict, closed=True):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource to be associated with verification request.</p>"""
    device_state: "aws_sdk_location.types.device_state.DeviceState"
    """<p>The device's state, including position, IP address, cell signals and Wi-Fi access points.</p>"""
    distance_unit: NotRequired["aws_sdk_location.types.distance_unit.DistanceUnit"]
    """<p>The distance unit for the verification request.</p> <p>Default Value: <code>Kilometers</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyDevicePositionRequest) -> dict:
    out: dict = {}
    import aws_sdk_location.types.device_state

    out["DeviceState"] = aws_sdk_location.types.device_state.serialize_json(
        value["device_state"]
    )
    if "distance_unit" in value:
        out["DistanceUnit"] = value["distance_unit"]
    return out


def deserialize_json(data: dict) -> VerifyDevicePositionRequest:
    out: VerifyDevicePositionRequest = {}  # type: ignore[typeddict-item]
    if "DeviceState" in data:
        import aws_sdk_location.types.device_state

        out["device_state"] = aws_sdk_location.types.device_state.deserialize_json(
            data["DeviceState"]
        )
    else:
        raise DeserializationError("VerifyDevicePositionRequest.device_state required")
    if "DistanceUnit" in data:
        out["distance_unit"] = data["DistanceUnit"]
    return out
