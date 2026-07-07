"""Generated from Smithy shape ``com.amazonaws.mediastore#GetContainerPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_policy


class GetContainerPolicyOutput(TypedDict, closed=True):
    policy: "aws_sdk_mediastore.types.container_policy.ContainerPolicy"
    """<p>The contents of the access policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerPolicyOutput) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerPolicyOutput:
    out: GetContainerPolicyOutput = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("GetContainerPolicyOutput.policy required")
    return out
