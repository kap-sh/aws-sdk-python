"""Generated from Smithy shape ``com.amazonaws.mediastore#GetLifecyclePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediastore.types.container_name


class GetLifecyclePolicyInput(TypedDict, closed=True):
    container_name: "capo_mediastore.types.container_name.ContainerName"
    """<p>The name of the container that the object lifecycle policy is assigned to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLifecyclePolicyInput) -> dict:
    out: dict = {}
    out["ContainerName"] = value["container_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLifecyclePolicyInput:
    out: GetLifecyclePolicyInput = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    else:
        raise DeserializationError("GetLifecyclePolicyInput.container_name required")
    return out
