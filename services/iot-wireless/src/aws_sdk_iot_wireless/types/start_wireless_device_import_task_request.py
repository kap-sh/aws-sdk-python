"""Generated from Smithy shape ``com.amazonaws.iotwireless#StartWirelessDeviceImportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.client_request_token
    import aws_sdk_iot_wireless.types.destination_name
    import aws_sdk_iot_wireless.types.positioning_config_status
    import aws_sdk_iot_wireless.types.sidewalk_start_import_info
    import aws_sdk_iot_wireless.types.tag_list


class StartWirelessDeviceImportTaskRequest(TypedDict):
    destination_name: "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    """<p>The name of the Sidewalk destination that describes the IoT rule to route messages from the devices in the import task that are onboarded to AWS IoT Wireless.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    tags: NotRequired["aws_sdk_iot_wireless.types.tag_list.TagList"]
    positioning: NotRequired[
        "aws_sdk_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
    ]
    """<p>The integration status of the Device Location feature for Sidewalk devices.</p>"""
    sidewalk: (
        "aws_sdk_iot_wireless.types.sidewalk_start_import_info.SidewalkStartImportInfo"
    )
    """<p>The Sidewalk-related parameters for importing wireless devices that need to be provisioned in bulk.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartWirelessDeviceImportTaskRequest) -> dict:
    out: dict = {}
    out["DestinationName"] = value["destination_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_iot_wireless.types.tag_list

        out["Tags"] = aws_sdk_iot_wireless.types.tag_list.serialize_json(value["tags"])
    if "positioning" in value:
        import aws_sdk_iot_wireless.types.positioning_config_status

        out["Positioning"] = (
            aws_sdk_iot_wireless.types.positioning_config_status.serialize_json(
                value["positioning"]
            )
        )
    import aws_sdk_iot_wireless.types.sidewalk_start_import_info

    out["Sidewalk"] = (
        aws_sdk_iot_wireless.types.sidewalk_start_import_info.serialize_json(
            value["sidewalk"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartWirelessDeviceImportTaskRequest:
    out: StartWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    else:
        raise DeserializationError(
            "StartWirelessDeviceImportTaskRequest.destination_name required"
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import aws_sdk_iot_wireless.types.tag_list

        out["tags"] = aws_sdk_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    if "Positioning" in data:
        import aws_sdk_iot_wireless.types.positioning_config_status

        out["positioning"] = (
            aws_sdk_iot_wireless.types.positioning_config_status.deserialize_json(
                data["Positioning"]
            )
        )
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_start_import_info

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_start_import_info.deserialize_json(
                data["Sidewalk"]
            )
        )
    else:
        raise DeserializationError(
            "StartWirelessDeviceImportTaskRequest.sidewalk required"
        )
    return out
