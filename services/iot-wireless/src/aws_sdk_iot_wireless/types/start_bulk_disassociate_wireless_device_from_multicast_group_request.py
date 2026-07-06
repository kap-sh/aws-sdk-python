"""Generated from Smithy shape ``com.amazonaws.iotwireless#StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.multicast_group_id
    import aws_sdk_iot_wireless.types.query_string
    import aws_sdk_iot_wireless.types.tag_list


class StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest(
    TypedDict, closed=True
):
    id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId"
    query_string: NotRequired["aws_sdk_iot_wireless.types.query_string.QueryString"]
    tags: NotRequired["aws_sdk_iot_wireless.types.tag_list.TagList"]


# --- restJson1 ser/de ---
def serialize_json(
    value: StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest,
) -> dict:
    out: dict = {}
    if "query_string" in value:
        out["QueryString"] = value["query_string"]
    if "tags" in value:
        import aws_sdk_iot_wireless.types.tag_list

        out["Tags"] = aws_sdk_iot_wireless.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(
    data: dict,
) -> StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest:
    out: StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest = {}  # type: ignore[typeddict-item]
    if "QueryString" in data:
        out["query_string"] = data["QueryString"]
    if "Tags" in data:
        import aws_sdk_iot_wireless.types.tag_list

        out["tags"] = aws_sdk_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    return out
