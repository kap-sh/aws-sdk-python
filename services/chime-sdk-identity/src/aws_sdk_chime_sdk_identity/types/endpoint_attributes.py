"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#EndpointAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.non_empty_sensitive_string1600


class EndpointAttributes(TypedDict):
    device_token: "aws_sdk_chime_sdk_identity.types.non_empty_sensitive_string1600.NonEmptySensitiveString1600"
    """<p>The device token for the GCM, APNS, and APNS_SANDBOX endpoint types.</p>"""
    voip_device_token: NotRequired[
        "aws_sdk_chime_sdk_identity.types.non_empty_sensitive_string1600.NonEmptySensitiveString1600"
    ]
    """<p>The VOIP device token for the APNS and APNS_SANDBOX endpoint types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointAttributes) -> dict:
    out: dict = {}
    out["DeviceToken"] = value["device_token"]
    if "voip_device_token" in value:
        out["VoipDeviceToken"] = value["voip_device_token"]
    return out


def deserialize_json(data: dict) -> EndpointAttributes:
    out: EndpointAttributes = {}  # type: ignore[typeddict-item]
    if "DeviceToken" in data:
        out["device_token"] = data["DeviceToken"]
    else:
        raise DeserializationError("EndpointAttributes.device_token required")
    if "VoipDeviceToken" in data:
        out["voip_device_token"] = data["VoipDeviceToken"]
    return out
