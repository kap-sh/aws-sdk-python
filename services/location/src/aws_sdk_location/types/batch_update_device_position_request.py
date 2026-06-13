"""Generated from Smithy shape ``com.amazonaws.location#BatchUpdateDevicePositionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.device_position_update_list
    import aws_sdk_location.types.resource_name


class BatchUpdateDevicePositionRequest(TypedDict):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource to update.</p>"""
    updates: (
        "aws_sdk_location.types.device_position_update_list.DevicePositionUpdateList"
    )
    """<p>Contains the position update details for each device, up to 10 devices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDevicePositionRequest) -> dict:
    out: dict = {}
    import aws_sdk_location.types.device_position_update_list

    out["Updates"] = aws_sdk_location.types.device_position_update_list.serialize_json(
        value["updates"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateDevicePositionRequest:
    out: BatchUpdateDevicePositionRequest = {}  # type: ignore[typeddict-item]
    if "Updates" in data:
        import aws_sdk_location.types.device_position_update_list

        out["updates"] = (
            aws_sdk_location.types.device_position_update_list.deserialize_json(
                data["Updates"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateDevicePositionRequest.updates required")
    return out
