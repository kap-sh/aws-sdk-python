"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DomainPatterns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.domain_pattern

DomainPatterns: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.domain_pattern.DomainPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainPatterns) -> list:
    return list(value)


def deserialize_json(data: list) -> DomainPatterns:
    return list(data)
