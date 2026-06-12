"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateDeviceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.client_request_token
    import aws_sdk_iot_wireless.types.device_profile_name
    import aws_sdk_iot_wireless.types.lo_ra_wan_device_profile
    import aws_sdk_iot_wireless.types.sidewalk_create_device_profile
    import aws_sdk_iot_wireless.types.tag_list


class CreateDeviceProfileRequest(TypedDict):
    name: NotRequired[
        "aws_sdk_iot_wireless.types.device_profile_name.DeviceProfileName"
    ]
    """<p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>"""
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_device_profile.LoRaWANDeviceProfile"
    ]
    """<p>The device profile information to use to create the device profile.</p>"""
    tags: NotRequired["aws_sdk_iot_wireless.types.tag_list.TagList"]
    """<p>The tags to attach to the new device profile. Tags are metadata that you can use to manage a resource.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    """<p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>"""
    sidewalk: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_create_device_profile.SidewalkCreateDeviceProfile"
    ]
    """<p>The Sidewalk-related information for creating the Sidewalk device profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeviceProfileRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_device_profile

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_device_profile.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "tags" in value:
        import aws_sdk_iot_wireless.types.tag_list

        out["Tags"] = aws_sdk_iot_wireless.types.tag_list.serialize_json(value["tags"])
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "sidewalk" in value:
        import aws_sdk_iot_wireless.types.sidewalk_create_device_profile

        out["Sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_create_device_profile.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDeviceProfileRequest:
    out: CreateDeviceProfileRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_device_profile

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_device_profile.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "Tags" in data:
        import aws_sdk_iot_wireless.types.tag_list

        out["tags"] = aws_sdk_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_create_device_profile

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_create_device_profile.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
