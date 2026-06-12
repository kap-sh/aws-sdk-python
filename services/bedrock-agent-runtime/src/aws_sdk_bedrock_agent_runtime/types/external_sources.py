"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ExternalSources``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.external_source

ExternalSources: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.external_source.ExternalSource"]


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSources) -> list:
    import aws_sdk_bedrock_agent_runtime.types.external_source
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.external_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExternalSources:
    import aws_sdk_bedrock_agent_runtime.types.external_source
    out: ExternalSources = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.external_source.deserialize_json(item))
    return out