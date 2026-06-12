"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SeedUrls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.seed_url

SeedUrls: TypeAlias = list["aws_sdk_bedrock_agent.types.seed_url.SeedUrl"]


# --- restJson1 ser/de ---
def serialize_json(value: SeedUrls) -> list:
    import aws_sdk_bedrock_agent.types.seed_url

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.seed_url.serialize_json(item))
    return out


def deserialize_json(data: list) -> SeedUrls:
    import aws_sdk_bedrock_agent.types.seed_url

    out: SeedUrls = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.seed_url.deserialize_json(item))
    return out
