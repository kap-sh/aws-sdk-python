"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SeedUrls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.seed_url

SeedUrls: TypeAlias = list["capo_bedrock_agent.types.seed_url.SeedUrl"]


# --- restJson1 ser/de ---
def serialize_json(value: SeedUrls) -> list:
    import capo_bedrock_agent.types.seed_url

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.seed_url.serialize_json(item))
    return out


def deserialize_json(data: list) -> SeedUrls:
    import capo_bedrock_agent.types.seed_url

    out: SeedUrls = []
    for item in data:
        out.append(capo_bedrock_agent.types.seed_url.deserialize_json(item))
    return out
