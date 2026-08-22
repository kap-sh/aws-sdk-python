"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerationAssets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.policy_generation_asset

PolicyGenerationAssets: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.policy_generation_asset.PolicyGenerationAsset"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationAssets) -> list:
    import capo_bedrock_agentcore_control.types.policy_generation_asset

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.policy_generation_asset.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PolicyGenerationAssets:
    import capo_bedrock_agentcore_control.types.policy_generation_asset

    out: PolicyGenerationAssets = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.policy_generation_asset.deserialize_json(
                item
            )
        )
    return out
