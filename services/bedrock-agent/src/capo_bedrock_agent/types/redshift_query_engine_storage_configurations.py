"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftQueryEngineStorageConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.redshift_query_engine_storage_configuration

RedshiftQueryEngineStorageConfigurations: TypeAlias = list[
    "capo_bedrock_agent.types.redshift_query_engine_storage_configuration.RedshiftQueryEngineStorageConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftQueryEngineStorageConfigurations) -> list:
    import capo_bedrock_agent.types.redshift_query_engine_storage_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.redshift_query_engine_storage_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RedshiftQueryEngineStorageConfigurations:
    import capo_bedrock_agent.types.redshift_query_engine_storage_configuration

    out: RedshiftQueryEngineStorageConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.redshift_query_engine_storage_configuration.deserialize_json(
                item
            )
        )
    return out
