"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetRegistryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.registry_identifier


class GetRegistryRequest(TypedDict, closed=True):
    registry_id: (
        "aws_sdk_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry to retrieve. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRegistryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRegistryRequest:
    out: GetRegistryRequest = {}  # type: ignore[typeddict-item]
    return out
