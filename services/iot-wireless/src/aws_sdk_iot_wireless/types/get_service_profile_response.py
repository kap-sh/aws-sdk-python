"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetServiceProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_get_service_profile_info
    import aws_sdk_iot_wireless.types.service_profile_arn
    import aws_sdk_iot_wireless.types.service_profile_id
    import aws_sdk_iot_wireless.types.service_profile_name


class GetServiceProfileResponse(TypedDict):
    arn: NotRequired["aws_sdk_iot_wireless.types.service_profile_arn.ServiceProfileArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    name: NotRequired[
        "aws_sdk_iot_wireless.types.service_profile_name.ServiceProfileName"
    ]
    """<p>The name of the resource.</p>"""
    id: NotRequired["aws_sdk_iot_wireless.types.service_profile_id.ServiceProfileId"]
    """<p>The ID of the service profile.</p>"""
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_get_service_profile_info.LoRaWANGetServiceProfileInfo"
    ]
    """<p>Information about the service profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceProfileResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_get_service_profile_info

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_get_service_profile_info.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetServiceProfileResponse:
    out: GetServiceProfileResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_get_service_profile_info

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_get_service_profile_info.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
