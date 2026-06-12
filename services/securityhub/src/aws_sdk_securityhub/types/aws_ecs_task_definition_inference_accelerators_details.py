"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionInferenceAcceleratorsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionInferenceAcceleratorsDetails(TypedDict):
    device_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Elastic Inference accelerator device name.</p>"""
    device_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Elastic Inference accelerator type to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionInferenceAcceleratorsDetails) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "device_type" in value:
        out["DeviceType"] = value["device_type"]
    return out


def deserialize_json(data: dict) -> AwsEcsTaskDefinitionInferenceAcceleratorsDetails:
    out: AwsEcsTaskDefinitionInferenceAcceleratorsDetails = {}  # type: ignore[typeddict-item]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "DeviceType" in data:
        out["device_type"] = data["DeviceType"]
    return out
