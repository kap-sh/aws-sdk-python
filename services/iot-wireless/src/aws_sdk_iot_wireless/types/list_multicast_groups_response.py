"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListMulticastGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.multicast_group_list
    import aws_sdk_iot_wireless.types.next_token


class ListMulticastGroupsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    multicast_group_list: NotRequired[
        "aws_sdk_iot_wireless.types.multicast_group_list.MulticastGroupList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListMulticastGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "multicast_group_list" in value:
        import aws_sdk_iot_wireless.types.multicast_group_list

        out["MulticastGroupList"] = (
            aws_sdk_iot_wireless.types.multicast_group_list.serialize_json(
                value["multicast_group_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListMulticastGroupsResponse:
    out: ListMulticastGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MulticastGroupList" in data:
        import aws_sdk_iot_wireless.types.multicast_group_list

        out["multicast_group_list"] = (
            aws_sdk_iot_wireless.types.multicast_group_list.deserialize_json(
                data["MulticastGroupList"]
            )
        )
    return out
