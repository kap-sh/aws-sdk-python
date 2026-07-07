"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetMulticastGroupSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_multicast_session


class GetMulticastGroupSessionResponse(TypedDict, closed=True):
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_multicast_session.LoRaWANMulticastSession"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetMulticastGroupSessionResponse) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_multicast_session

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_multicast_session.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMulticastGroupSessionResponse:
    out: GetMulticastGroupSessionResponse = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_multicast_session

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_multicast_session.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
