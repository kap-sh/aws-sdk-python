"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingConnectivityDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.connectivity_status
    import aws_sdk_iot_managed_integrations.types.connectivity_timestamp
    import aws_sdk_iot_managed_integrations.types.disconnect_reason_value
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class GetManagedThingConnectivityDataResponse(TypedDict, closed=True):
    managed_thing_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The id of a managed thing.</p>"""
    connected: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connectivity_status.ConnectivityStatus"
    ]
    """<p>The connectivity status for a managed thing.</p>"""
    timestamp: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connectivity_timestamp.ConnectivityTimestamp"
    ]
    """<p>The timestamp value of when the connectivity status for a managed thing was last taken.</p>"""
    disconnect_reason: NotRequired[
        "aws_sdk_iot_managed_integrations.types.disconnect_reason_value.DisconnectReasonValue"
    ]
    """<p>The reason for the connectivity disconnect with the managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingConnectivityDataResponse) -> dict:
    out: dict = {}
    if "managed_thing_id" in value:
        out["ManagedThingId"] = value["managed_thing_id"]
    if "connected" in value:
        out["Connected"] = value["connected"]
    if "timestamp" in value:
        import aws_sdk_iot_managed_integrations.types.connectivity_timestamp

        out["Timestamp"] = (
            aws_sdk_iot_managed_integrations.types.connectivity_timestamp.serialize_json(
                value["timestamp"]
            )
        )
    if "disconnect_reason" in value:
        import aws_sdk_iot_managed_integrations.types.disconnect_reason_value

        out["DisconnectReason"] = (
            aws_sdk_iot_managed_integrations.types.disconnect_reason_value.serialize_json(
                value["disconnect_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetManagedThingConnectivityDataResponse:
    out: GetManagedThingConnectivityDataResponse = {}  # type: ignore[typeddict-item]
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    if "Connected" in data:
        out["connected"] = data["Connected"]
    if "Timestamp" in data:
        import aws_sdk_iot_managed_integrations.types.connectivity_timestamp

        out["timestamp"] = (
            aws_sdk_iot_managed_integrations.types.connectivity_timestamp.deserialize_json(
                data["Timestamp"]
            )
        )
    if "DisconnectReason" in data:
        import aws_sdk_iot_managed_integrations.types.disconnect_reason_value

        out["disconnect_reason"] = (
            aws_sdk_iot_managed_integrations.types.disconnect_reason_value.deserialize_json(
                data["DisconnectReason"]
            )
        )
    return out
