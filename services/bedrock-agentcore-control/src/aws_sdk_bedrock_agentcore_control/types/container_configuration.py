"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ContainerConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.runtime_container_uri


class ContainerConfiguration(TypedDict):
    container_uri: "aws_sdk_bedrock_agentcore_control.types.runtime_container_uri.RuntimeContainerUri"
    """<p>The ECR URI of the container.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerConfiguration) -> dict:
    out: dict = {}
    out["containerUri"] = value["container_uri"]
    return out


def deserialize_json(data: dict) -> ContainerConfiguration:
    out: ContainerConfiguration = {}  # type: ignore[typeddict-item]
    if "containerUri" in data:
        out["container_uri"] = data["containerUri"]
    else:
        raise DeserializationError("ContainerConfiguration.container_uri required")
    return out
