"""Generated from Smithy shape ``com.amazonaws.braket#DeviceConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.string256


class DeviceConfig(TypedDict):
    device: "aws_sdk_braket.types.string256.String256"
    """<p>The primary device ARN used to create and run an Amazon Braket hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceConfig) -> dict:
    out: dict = {}
    out["device"] = value["device"]
    return out


def deserialize_json(data: dict) -> DeviceConfig:
    out: DeviceConfig = {}  # type: ignore[typeddict-item]
    if "device" in data:
        out["device"] = data["device"]
    else:
        raise DeserializationError("DeviceConfig.device required")
    return out
