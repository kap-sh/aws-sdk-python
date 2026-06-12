"""Generated from Smithy shape ``com.amazonaws.mediastore#PutLifecyclePolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_name
    import aws_sdk_mediastore.types.lifecycle_policy


class PutLifecyclePolicyInput(TypedDict):
    container_name: "aws_sdk_mediastore.types.container_name.ContainerName"
    """<p>The name of the container that you want to assign the object lifecycle policy to.</p>"""
    lifecycle_policy: "aws_sdk_mediastore.types.lifecycle_policy.LifecyclePolicy"
    """<p>The object lifecycle policy to apply to the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLifecyclePolicyInput) -> dict:
    out: dict = {}
    out["ContainerName"] = value["container_name"]
    out["LifecyclePolicy"] = value["lifecycle_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLifecyclePolicyInput:
    out: PutLifecyclePolicyInput = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    else:
        raise DeserializationError("PutLifecyclePolicyInput.container_name required")
    if "LifecyclePolicy" in data:
        out["lifecycle_policy"] = data["LifecyclePolicy"]
    else:
        raise DeserializationError("PutLifecyclePolicyInput.lifecycle_policy required")
    return out
