"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListWirelessGatewaysResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.next_token
    import aws_sdk_iot_wireless.types.wireless_gateway_statistics_list


class ListWirelessGatewaysResponse(TypedDict):
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""
    wireless_gateway_list: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_statistics_list.WirelessGatewayStatisticsList"
    ]
    """<p>The ID of the wireless gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWirelessGatewaysResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "wireless_gateway_list" in value:
        import aws_sdk_iot_wireless.types.wireless_gateway_statistics_list

        out["WirelessGatewayList"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_statistics_list.serialize_json(
                value["wireless_gateway_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListWirelessGatewaysResponse:
    out: ListWirelessGatewaysResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "WirelessGatewayList" in data:
        import aws_sdk_iot_wireless.types.wireless_gateway_statistics_list

        out["wireless_gateway_list"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_statistics_list.deserialize_json(
                data["WirelessGatewayList"]
            )
        )
    return out
