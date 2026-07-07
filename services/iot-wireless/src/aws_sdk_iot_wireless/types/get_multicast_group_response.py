"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetMulticastGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.created_at
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.lo_ra_wan_multicast_get
    import aws_sdk_iot_wireless.types.multicast_group_arn
    import aws_sdk_iot_wireless.types.multicast_group_id
    import aws_sdk_iot_wireless.types.multicast_group_name
    import aws_sdk_iot_wireless.types.multicast_group_status


class GetMulticastGroupResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_iot_wireless.types.multicast_group_arn.MulticastGroupArn"]
    id: NotRequired["aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId"]
    name: NotRequired[
        "aws_sdk_iot_wireless.types.multicast_group_name.MulticastGroupName"
    ]
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    status: NotRequired[
        "aws_sdk_iot_wireless.types.multicast_group_status.MulticastGroupStatus"
    ]
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_multicast_get.LoRaWANMulticastGet"
    ]
    created_at: NotRequired["aws_sdk_iot_wireless.types.created_at.CreatedAt"]


# --- restJson1 ser/de ---
def serialize_json(value: GetMulticastGroupResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        out["Status"] = value["status"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_multicast_get

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_multicast_get.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "created_at" in value:
        import aws_sdk_iot_wireless.types.created_at

        out["CreatedAt"] = aws_sdk_iot_wireless.types.created_at.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> GetMulticastGroupResponse:
    out: GetMulticastGroupResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_multicast_get

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_multicast_get.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_iot_wireless.types.created_at

        out["created_at"] = aws_sdk_iot_wireless.types.created_at.deserialize_json(
            data["CreatedAt"]
        )
    return out
