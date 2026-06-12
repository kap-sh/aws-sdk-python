"""Generated from Smithy shape ``com.amazonaws.mediastore#GetLifecyclePolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.lifecycle_policy


class GetLifecyclePolicyOutput(TypedDict):
    lifecycle_policy: "aws_sdk_mediastore.types.lifecycle_policy.LifecyclePolicy"
    """<p>The object lifecycle policy that is assigned to the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLifecyclePolicyOutput) -> dict:
    out: dict = {}
    out["LifecyclePolicy"] = value["lifecycle_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLifecyclePolicyOutput:
    out: GetLifecyclePolicyOutput = {}  # type: ignore[typeddict-item]
    if "LifecyclePolicy" in data:
        out["lifecycle_policy"] = data["LifecyclePolicy"]
    else:
        raise DeserializationError("GetLifecyclePolicyOutput.lifecycle_policy required")
    return out
