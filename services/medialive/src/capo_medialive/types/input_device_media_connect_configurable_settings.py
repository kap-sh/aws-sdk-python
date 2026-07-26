"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceMediaConnectConfigurableSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class InputDeviceMediaConnectConfigurableSettings(TypedDict, closed=True):
    flow_arn: NotRequired["capo_medialive.types.__string.__string"]
    """The ARN of the MediaConnect flow to attach this device to."""
    role_arn: NotRequired["capo_medialive.types.__string.__string"]
    """The ARN for the role that MediaLive assumes to access the attached flow and secret. For more information about how to create this role, see the MediaLive user guide."""
    secret_arn: NotRequired["capo_medialive.types.__string.__string"]
    """The ARN for the secret that holds the encryption key to encrypt the content output by the device."""
    source_name: NotRequired["capo_medialive.types.__string.__string"]
    """The name of the MediaConnect Flow source to stream to."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceMediaConnectConfigurableSettings) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    return out


def deserialize_json(data: dict) -> InputDeviceMediaConnectConfigurableSettings:
    out: InputDeviceMediaConnectConfigurableSettings = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    if "sourceName" in data:
        out["source_name"] = data["sourceName"]
    return out
