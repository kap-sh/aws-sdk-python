"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListDestinationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.destination_list
    import aws_sdk_iot_wireless.types.next_token


class ListDestinationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""
    destination_list: NotRequired[
        "aws_sdk_iot_wireless.types.destination_list.DestinationList"
    ]
    """<p>The list of destinations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDestinationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "destination_list" in value:
        import aws_sdk_iot_wireless.types.destination_list

        out["DestinationList"] = (
            aws_sdk_iot_wireless.types.destination_list.serialize_json(
                value["destination_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDestinationsResponse:
    out: ListDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DestinationList" in data:
        import aws_sdk_iot_wireless.types.destination_list

        out["destination_list"] = (
            aws_sdk_iot_wireless.types.destination_list.deserialize_json(
                data["DestinationList"]
            )
        )
    return out
