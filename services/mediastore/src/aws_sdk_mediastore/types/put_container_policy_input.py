"""Generated from Smithy shape ``com.amazonaws.mediastore#PutContainerPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_name
    import aws_sdk_mediastore.types.container_policy


class PutContainerPolicyInput(TypedDict):
    container_name: "aws_sdk_mediastore.types.container_name.ContainerName"
    """<p>The name of the container.</p>"""
    policy: "aws_sdk_mediastore.types.container_policy.ContainerPolicy"
    """<p>The contents of the policy, which includes the following: </p> <ul> <li> <p>One <code>Version</code> tag</p> </li> <li> <p>One <code>Statement</code> tag that contains the standard tags for the policy.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutContainerPolicyInput) -> dict:
    out: dict = {}
    out["ContainerName"] = value["container_name"]
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutContainerPolicyInput:
    out: PutContainerPolicyInput = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    else:
        raise DeserializationError("PutContainerPolicyInput.container_name required")
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutContainerPolicyInput.policy required")
    return out
