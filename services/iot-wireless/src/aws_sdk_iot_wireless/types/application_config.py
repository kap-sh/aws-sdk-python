"""Generated from Smithy shape ``com.amazonaws.iotwireless#ApplicationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.application_config_type
    import aws_sdk_iot_wireless.types.destination_name
    import aws_sdk_iot_wireless.types.f_port


class ApplicationConfig(TypedDict, closed=True):
    f_port: NotRequired["aws_sdk_iot_wireless.types.f_port.FPort"]
    type: NotRequired[
        "aws_sdk_iot_wireless.types.application_config_type.ApplicationConfigType"
    ]
    """<p>Application type, which can be specified to obtain real-time position information of your LoRaWAN device.</p>"""
    destination_name: NotRequired[
        "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The name of the position data destination that describes the AWS IoT rule that processes the device's position data for use by AWS IoT Core for LoRaWAN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationConfig) -> dict:
    out: dict = {}
    if "f_port" in value:
        out["FPort"] = value["f_port"]
    if "type" in value:
        import aws_sdk_iot_wireless.types.application_config_type

        out["Type"] = aws_sdk_iot_wireless.types.application_config_type.serialize_json(
            value["type"]
        )
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    return out


def deserialize_json(data: dict) -> ApplicationConfig:
    out: ApplicationConfig = {}  # type: ignore[typeddict-item]
    if "FPort" in data:
        out["f_port"] = data["FPort"]
    if "Type" in data:
        import aws_sdk_iot_wireless.types.application_config_type

        out["type"] = (
            aws_sdk_iot_wireless.types.application_config_type.deserialize_json(
                data["Type"]
            )
        )
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    return out
