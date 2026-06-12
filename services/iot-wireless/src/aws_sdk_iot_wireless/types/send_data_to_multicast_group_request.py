"""Generated from Smithy shape ``com.amazonaws.iotwireless#SendDataToMulticastGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.multicast_group_id
    import aws_sdk_iot_wireless.types.multicast_wireless_metadata
    import aws_sdk_iot_wireless.types.payload_data


class SendDataToMulticastGroupRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId"
    payload_data: "aws_sdk_iot_wireless.types.payload_data.PayloadData"
    wireless_metadata: "aws_sdk_iot_wireless.types.multicast_wireless_metadata.MulticastWirelessMetadata"


# --- restJson1 ser/de ---
def serialize_json(value: SendDataToMulticastGroupRequest) -> dict:
    out: dict = {}
    out["PayloadData"] = value["payload_data"]
    import aws_sdk_iot_wireless.types.multicast_wireless_metadata

    out["WirelessMetadata"] = (
        aws_sdk_iot_wireless.types.multicast_wireless_metadata.serialize_json(
            value["wireless_metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> SendDataToMulticastGroupRequest:
    out: SendDataToMulticastGroupRequest = {}  # type: ignore[typeddict-item]
    if "PayloadData" in data:
        out["payload_data"] = data["PayloadData"]
    else:
        raise DeserializationError(
            "SendDataToMulticastGroupRequest.payload_data required"
        )
    if "WirelessMetadata" in data:
        import aws_sdk_iot_wireless.types.multicast_wireless_metadata

        out["wireless_metadata"] = (
            aws_sdk_iot_wireless.types.multicast_wireless_metadata.deserialize_json(
                data["WirelessMetadata"]
            )
        )
    else:
        raise DeserializationError(
            "SendDataToMulticastGroupRequest.wireless_metadata required"
        )
    return out
