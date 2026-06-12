"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateWirelessGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.client_request_token
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.lo_ra_wan_gateway
    import aws_sdk_iot_wireless.types.tag_list
    import aws_sdk_iot_wireless.types.wireless_gateway_name


class CreateWirelessGatewayRequest(TypedDict):
    name: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_name.WirelessGatewayName"
    ]
    """<p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>"""
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    """<p>The description of the new resource.</p>"""
    lo_ra_wan: "aws_sdk_iot_wireless.types.lo_ra_wan_gateway.LoRaWANGateway"
    """<p>The gateway configuration information to use to create the wireless gateway.</p>"""
    tags: NotRequired["aws_sdk_iot_wireless.types.tag_list.TagList"]
    """<p>The tags to attach to the new wireless gateway. Tags are metadata that you can use to manage a resource.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    """<p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWirelessGatewayRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_iot_wireless.types.lo_ra_wan_gateway

    out["LoRaWAN"] = aws_sdk_iot_wireless.types.lo_ra_wan_gateway.serialize_json(
        value["lo_ra_wan"]
    )
    if "tags" in value:
        import aws_sdk_iot_wireless.types.tag_list

        out["Tags"] = aws_sdk_iot_wireless.types.tag_list.serialize_json(value["tags"])
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateWirelessGatewayRequest:
    out: CreateWirelessGatewayRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_gateway

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_gateway.deserialize_json(
                data["LoRaWAN"]
            )
        )
    else:
        raise DeserializationError("CreateWirelessGatewayRequest.lo_ra_wan required")
    if "Tags" in data:
        import aws_sdk_iot_wireless.types.tag_list

        out["tags"] = aws_sdk_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
