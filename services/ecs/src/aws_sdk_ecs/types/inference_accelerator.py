"""Generated from Smithy shape ``com.amazonaws.ecs#InferenceAccelerator``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class InferenceAccelerator(TypedDict, closed=True):
    device_name: "aws_sdk_ecs.types.string.String"
    r"""<p>The Elastic Inference accelerator device name. The <code>deviceName</code> must also be referenced in a container definition as a <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ResourceRequirement.html\">ResourceRequirement</a>.</p>"""
    device_type: "aws_sdk_ecs.types.string.String"
    """<p>The Elastic Inference accelerator type to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceAccelerator) -> dict:
    out: dict = {}
    out["deviceName"] = value["device_name"]
    out["deviceType"] = value["device_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceAccelerator:
    out: InferenceAccelerator = {}  # type: ignore[typeddict-item]
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    else:
        raise DeserializationError("InferenceAccelerator.device_name required")
    if "deviceType" in data:
        out["device_type"] = data["deviceType"]
    else:
        raise DeserializationError("InferenceAccelerator.device_type required")
    return out
