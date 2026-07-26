"""Generated from Smithy shape ``com.amazonaws.bedrock#ExternalSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.external_source

ExternalSources: TypeAlias = list["capo_bedrock.types.external_source.ExternalSource"]


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSources) -> list:
    import capo_bedrock.types.external_source

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.external_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExternalSources:
    import capo_bedrock.types.external_source

    out: ExternalSources = []
    for item in data:
        out.append(capo_bedrock.types.external_source.deserialize_json(item))
    return out
