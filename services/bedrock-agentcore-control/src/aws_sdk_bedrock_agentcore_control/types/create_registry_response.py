"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateRegistryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.registry_arn


class CreateRegistryResponse(TypedDict):
    registry_arn: "aws_sdk_bedrock_agentcore_control.types.registry_arn.RegistryArn"
    """<p>The Amazon Resource Name (ARN) of the created registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRegistryResponse) -> dict:
    out: dict = {}
    out["registryArn"] = value["registry_arn"]
    return out


def deserialize_json(data: dict) -> CreateRegistryResponse:
    out: CreateRegistryResponse = {}  # type: ignore[typeddict-item]
    if "registryArn" in data:
        out["registry_arn"] = data["registryArn"]
    else:
        raise DeserializationError("CreateRegistryResponse.registry_arn required")
    return out
