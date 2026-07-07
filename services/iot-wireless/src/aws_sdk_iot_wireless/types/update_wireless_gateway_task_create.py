"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateWirelessGatewayTaskCreate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_create
    import aws_sdk_iot_wireless.types.update_data_source


class UpdateWirelessGatewayTaskCreate(TypedDict, closed=True):
    update_data_source: NotRequired[
        "aws_sdk_iot_wireless.types.update_data_source.UpdateDataSource"
    ]
    """<p>The link to the S3 bucket.</p>"""
    update_data_role: NotRequired[
        "aws_sdk_iot_wireless.types.update_data_source.UpdateDataSource"
    ]
    """<p>The IAM role used to read data from the S3 bucket.</p>"""
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_create.LoRaWANUpdateGatewayTaskCreate"
    ]
    """<p>The properties that relate to the LoRaWAN wireless gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWirelessGatewayTaskCreate) -> dict:
    out: dict = {}
    if "update_data_source" in value:
        out["UpdateDataSource"] = value["update_data_source"]
    if "update_data_role" in value:
        out["UpdateDataRole"] = value["update_data_role"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_create

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_create.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWirelessGatewayTaskCreate:
    out: UpdateWirelessGatewayTaskCreate = {}  # type: ignore[typeddict-item]
    if "UpdateDataSource" in data:
        out["update_data_source"] = data["UpdateDataSource"]
    if "UpdateDataRole" in data:
        out["update_data_role"] = data["UpdateDataRole"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_create

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_update_gateway_task_create.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
