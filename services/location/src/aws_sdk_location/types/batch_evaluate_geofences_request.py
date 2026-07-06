"""Generated from Smithy shape ``com.amazonaws.location#BatchEvaluateGeofencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.device_position_update_list
    import aws_sdk_location.types.resource_name


class BatchEvaluateGeofencesRequest(TypedDict, closed=True):
    collection_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The geofence collection used in evaluating the position of devices against its geofences.</p>"""
    device_position_updates: (
        "aws_sdk_location.types.device_position_update_list.DevicePositionUpdateList"
    )
    """<p>Contains device details for each device to be evaluated against the given geofence collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEvaluateGeofencesRequest) -> dict:
    out: dict = {}
    import aws_sdk_location.types.device_position_update_list

    out["DevicePositionUpdates"] = (
        aws_sdk_location.types.device_position_update_list.serialize_json(
            value["device_position_updates"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchEvaluateGeofencesRequest:
    out: BatchEvaluateGeofencesRequest = {}  # type: ignore[typeddict-item]
    if "DevicePositionUpdates" in data:
        import aws_sdk_location.types.device_position_update_list

        out["device_position_updates"] = (
            aws_sdk_location.types.device_position_update_list.deserialize_json(
                data["DevicePositionUpdates"]
            )
        )
    else:
        raise DeserializationError(
            "BatchEvaluateGeofencesRequest.device_position_updates required"
        )
    return out
