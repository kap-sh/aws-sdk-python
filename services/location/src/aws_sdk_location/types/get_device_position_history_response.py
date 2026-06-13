"""Generated from Smithy shape ``com.amazonaws.location#GetDevicePositionHistoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.device_position_list
    import aws_sdk_location.types.token


class GetDevicePositionHistoryResponse(TypedDict):
    device_positions: "aws_sdk_location.types.device_position_list.DevicePositionList"
    """<p>Contains the position history details for the requested device.</p>"""
    next_token: NotRequired["aws_sdk_location.types.token.Token"]
    """<p>A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDevicePositionHistoryResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.device_position_list

    out["DevicePositions"] = aws_sdk_location.types.device_position_list.serialize_json(
        value["device_positions"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDevicePositionHistoryResponse:
    out: GetDevicePositionHistoryResponse = {}  # type: ignore[typeddict-item]
    if "DevicePositions" in data:
        import aws_sdk_location.types.device_position_list

        out["device_positions"] = (
            aws_sdk_location.types.device_position_list.deserialize_json(
                data["DevicePositions"]
            )
        )
    else:
        raise DeserializationError(
            "GetDevicePositionHistoryResponse.device_positions required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
