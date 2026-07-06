"""Generated from Smithy shape ``com.amazonaws.iotwireless#MessageDeliveryStatusResourceTypeEventConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.sidewalk_resource_type_event_configuration


class MessageDeliveryStatusResourceTypeEventConfiguration(TypedDict, closed=True):
    sidewalk: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_resource_type_event_configuration.SidewalkResourceTypeEventConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MessageDeliveryStatusResourceTypeEventConfiguration) -> dict:
    out: dict = {}
    if "sidewalk" in value:
        import aws_sdk_iot_wireless.types.sidewalk_resource_type_event_configuration

        out["Sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_resource_type_event_configuration.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> MessageDeliveryStatusResourceTypeEventConfiguration:
    out: MessageDeliveryStatusResourceTypeEventConfiguration = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_resource_type_event_configuration

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_resource_type_event_configuration.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
