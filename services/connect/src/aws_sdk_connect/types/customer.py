"""Generated from Smithy shape ``com.amazonaws.connect#Customer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.device_info
    import aws_sdk_connect.types.participant_capabilities


class Customer(TypedDict):
    device_info: NotRequired["aws_sdk_connect.types.device_info.DeviceInfo"]
    """<p>Information regarding Customer’s device.</p>"""
    capabilities: NotRequired[
        "aws_sdk_connect.types.participant_capabilities.ParticipantCapabilities"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Customer) -> dict:
    out: dict = {}
    if "device_info" in value:
        import aws_sdk_connect.types.device_info

        out["DeviceInfo"] = aws_sdk_connect.types.device_info.serialize_json(
            value["device_info"]
        )
    if "capabilities" in value:
        import aws_sdk_connect.types.participant_capabilities

        out["Capabilities"] = (
            aws_sdk_connect.types.participant_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> Customer:
    out: Customer = {}  # type: ignore[typeddict-item]
    if "DeviceInfo" in data:
        import aws_sdk_connect.types.device_info

        out["device_info"] = aws_sdk_connect.types.device_info.deserialize_json(
            data["DeviceInfo"]
        )
    if "Capabilities" in data:
        import aws_sdk_connect.types.participant_capabilities

        out["capabilities"] = (
            aws_sdk_connect.types.participant_capabilities.deserialize_json(
                data["Capabilities"]
            )
        )
    return out
