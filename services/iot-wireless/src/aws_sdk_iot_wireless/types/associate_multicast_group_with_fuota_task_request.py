"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateMulticastGroupWithFuotaTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.fuota_task_id
    import aws_sdk_iot_wireless.types.multicast_group_id


class AssociateMulticastGroupWithFuotaTaskRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId"
    multicast_group_id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId"


# --- restJson1 ser/de ---
def serialize_json(value: AssociateMulticastGroupWithFuotaTaskRequest) -> dict:
    out: dict = {}
    out["MulticastGroupId"] = value["multicast_group_id"]
    return out


def deserialize_json(data: dict) -> AssociateMulticastGroupWithFuotaTaskRequest:
    out: AssociateMulticastGroupWithFuotaTaskRequest = {}  # type: ignore[typeddict-item]
    if "MulticastGroupId" in data:
        out["multicast_group_id"] = data["MulticastGroupId"]
    else:
        raise DeserializationError(
            "AssociateMulticastGroupWithFuotaTaskRequest.multicast_group_id required"
        )
    return out
