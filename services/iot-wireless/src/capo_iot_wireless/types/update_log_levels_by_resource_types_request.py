"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateLogLevelsByResourceTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task_log_option_list
    import capo_iot_wireless.types.log_level
    import capo_iot_wireless.types.wireless_device_log_option_list
    import capo_iot_wireless.types.wireless_gateway_log_option_list


class UpdateLogLevelsByResourceTypesRequest(TypedDict, closed=True):
    default_log_level: NotRequired["capo_iot_wireless.types.log_level.LogLevel"]
    fuota_task_log_options: NotRequired[
        "capo_iot_wireless.types.fuota_task_log_option_list.FuotaTaskLogOptionList"
    ]
    wireless_device_log_options: NotRequired[
        "capo_iot_wireless.types.wireless_device_log_option_list.WirelessDeviceLogOptionList"
    ]
    wireless_gateway_log_options: NotRequired[
        "capo_iot_wireless.types.wireless_gateway_log_option_list.WirelessGatewayLogOptionList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLogLevelsByResourceTypesRequest) -> dict:
    out: dict = {}
    if "default_log_level" in value:
        import capo_iot_wireless.types.log_level

        out["DefaultLogLevel"] = capo_iot_wireless.types.log_level.serialize_json(
            value["default_log_level"]
        )
    if "fuota_task_log_options" in value:
        import capo_iot_wireless.types.fuota_task_log_option_list

        out["FuotaTaskLogOptions"] = (
            capo_iot_wireless.types.fuota_task_log_option_list.serialize_json(
                value["fuota_task_log_options"]
            )
        )
    if "wireless_device_log_options" in value:
        import capo_iot_wireless.types.wireless_device_log_option_list

        out["WirelessDeviceLogOptions"] = (
            capo_iot_wireless.types.wireless_device_log_option_list.serialize_json(
                value["wireless_device_log_options"]
            )
        )
    if "wireless_gateway_log_options" in value:
        import capo_iot_wireless.types.wireless_gateway_log_option_list

        out["WirelessGatewayLogOptions"] = (
            capo_iot_wireless.types.wireless_gateway_log_option_list.serialize_json(
                value["wireless_gateway_log_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateLogLevelsByResourceTypesRequest:
    out: UpdateLogLevelsByResourceTypesRequest = {}  # type: ignore[typeddict-item]
    if "DefaultLogLevel" in data:
        import capo_iot_wireless.types.log_level

        out["default_log_level"] = capo_iot_wireless.types.log_level.deserialize_json(
            data["DefaultLogLevel"]
        )
    if "FuotaTaskLogOptions" in data:
        import capo_iot_wireless.types.fuota_task_log_option_list

        out["fuota_task_log_options"] = (
            capo_iot_wireless.types.fuota_task_log_option_list.deserialize_json(
                data["FuotaTaskLogOptions"]
            )
        )
    if "WirelessDeviceLogOptions" in data:
        import capo_iot_wireless.types.wireless_device_log_option_list

        out["wireless_device_log_options"] = (
            capo_iot_wireless.types.wireless_device_log_option_list.deserialize_json(
                data["WirelessDeviceLogOptions"]
            )
        )
    if "WirelessGatewayLogOptions" in data:
        import capo_iot_wireless.types.wireless_gateway_log_option_list

        out["wireless_gateway_log_options"] = (
            capo_iot_wireless.types.wireless_gateway_log_option_list.deserialize_json(
                data["WirelessGatewayLogOptions"]
            )
        )
    return out
