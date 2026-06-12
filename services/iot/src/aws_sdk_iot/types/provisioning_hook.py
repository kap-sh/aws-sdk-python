"""Generated from Smithy shape ``com.amazonaws.iot#ProvisioningHook``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.payload_version
    import aws_sdk_iot.types.target_arn


class ProvisioningHook(TypedDict):
    payload_version: NotRequired["aws_sdk_iot.types.payload_version.PayloadVersion"]
    """<p>The payload that was sent to the target function.</p> <p> <i>Note:</i> Only Lambda functions are currently supported.</p>"""
    target_arn: "aws_sdk_iot.types.target_arn.TargetArn"
    """<p>The ARN of the target function.</p> <p> <i>Note:</i> Only Lambda functions are currently supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningHook) -> dict:
    out: dict = {}
    if "payload_version" in value:
        out["payloadVersion"] = value["payload_version"]
    out["targetArn"] = value["target_arn"]
    return out


def deserialize_json(data: dict) -> ProvisioningHook:
    out: ProvisioningHook = {}  # type: ignore[typeddict-item]
    if "payloadVersion" in data:
        out["payload_version"] = data["payloadVersion"]
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("ProvisioningHook.target_arn required")
    return out
