"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceMediaConnectSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class InputDeviceMediaConnectSettings(TypedDict):
    flow_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the MediaConnect flow."""
    role_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN for the role that MediaLive assumes to access the attached flow and secret."""
    secret_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the secret used to encrypt the stream."""
    source_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the MediaConnect flow source."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceMediaConnectSettings) -> dict:
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


def deserialize_json(data: dict) -> InputDeviceMediaConnectSettings:
    out: InputDeviceMediaConnectSettings = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    if "sourceName" in data:
        out["source_name"] = data["sourceName"]
    return out
