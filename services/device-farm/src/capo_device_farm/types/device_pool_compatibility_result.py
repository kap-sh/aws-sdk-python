"""Generated from Smithy shape ``com.amazonaws.devicefarm#DevicePoolCompatibilityResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.boolean
    import capo_device_farm.types.device
    import capo_device_farm.types.incompatibility_messages


class DevicePoolCompatibilityResult(TypedDict, closed=True):
    device: NotRequired["capo_device_farm.types.device.Device"]
    """<p>The device (phone or tablet) to return information about.</p>"""
    compatible: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>Whether the result was compatible with the device pool.</p>"""
    incompatibility_messages: NotRequired[
        "capo_device_farm.types.incompatibility_messages.IncompatibilityMessages"
    ]
    """<p>Information about the compatibility.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DevicePoolCompatibilityResult) -> dict:
    out: dict = {}
    if "device" in value:
        import capo_device_farm.types.device

        out["device"] = capo_device_farm.types.device.serialize_aws_json_1_1(
            value["device"]
        )
    if "compatible" in value:
        out["compatible"] = value["compatible"]
    if "incompatibility_messages" in value:
        import capo_device_farm.types.incompatibility_messages

        out["incompatibilityMessages"] = (
            capo_device_farm.types.incompatibility_messages.serialize_aws_json_1_1(
                value["incompatibility_messages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DevicePoolCompatibilityResult:
    out: DevicePoolCompatibilityResult = {}  # type: ignore[typeddict-item]
    if "device" in data:
        import capo_device_farm.types.device

        out["device"] = capo_device_farm.types.device.deserialize_aws_json_1_1(
            data["device"]
        )
    if "compatible" in data:
        out["compatible"] = data["compatible"]
    if "incompatibilityMessages" in data:
        import capo_device_farm.types.incompatibility_messages

        out["incompatibility_messages"] = (
            capo_device_farm.types.incompatibility_messages.deserialize_aws_json_1_1(
                data["incompatibilityMessages"]
            )
        )
    return out
