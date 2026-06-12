"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#GetDeviceRegistrationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_edge.types.cache_ttl_seconds
    import aws_sdk_sagemaker_edge.types.device_registration


class GetDeviceRegistrationResult(TypedDict):
    device_registration: NotRequired[
        "aws_sdk_sagemaker_edge.types.device_registration.DeviceRegistration"
    ]
    """<p>Describes if the device is currently registered with SageMaker Edge Manager.</p>"""
    cache_ttl: NotRequired[
        "aws_sdk_sagemaker_edge.types.cache_ttl_seconds.CacheTTLSeconds"
    ]
    """<p>The amount of time, in seconds, that the registration status is stored on the device’s cache before it is refreshed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceRegistrationResult) -> dict:
    out: dict = {}
    if "device_registration" in value:
        out["DeviceRegistration"] = value["device_registration"]
    if "cache_ttl" in value:
        out["CacheTTL"] = value["cache_ttl"]
    return out


def deserialize_json(data: dict) -> GetDeviceRegistrationResult:
    out: GetDeviceRegistrationResult = {}  # type: ignore[typeddict-item]
    if "DeviceRegistration" in data:
        out["device_registration"] = data["DeviceRegistration"]
    if "CacheTTL" in data:
        out["cache_ttl"] = data["CacheTTL"]
    return out
