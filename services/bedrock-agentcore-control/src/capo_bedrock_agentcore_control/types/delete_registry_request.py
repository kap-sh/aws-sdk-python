"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteRegistryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.registry_identifier


class DeleteRegistryRequest(TypedDict, closed=True):
    registry_id: (
        "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry to delete. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRegistryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRegistryRequest:
    out: DeleteRegistryRequest = {}  # type: ignore[typeddict-item]
    return out
