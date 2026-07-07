"""Generated from Smithy shape ``com.amazonaws.mediastore#GetCorsPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_name


class GetCorsPolicyInput(TypedDict, closed=True):
    container_name: "aws_sdk_mediastore.types.container_name.ContainerName"
    """<p>The name of the container that the policy is assigned to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCorsPolicyInput) -> dict:
    out: dict = {}
    out["ContainerName"] = value["container_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCorsPolicyInput:
    out: GetCorsPolicyInput = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    else:
        raise DeserializationError("GetCorsPolicyInput.container_name required")
    return out
