"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankingMetadataSelectiveModeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.fields_for_reranking


class _RerankingMetadataSelectiveModeConfiguration_fieldsToInclude(
    TypedDict, closed=True
):
    fieldsToInclude: (
        "aws_sdk_bedrock_agent_runtime.types.fields_for_reranking.FieldsForReranking"
    )


class _RerankingMetadataSelectiveModeConfiguration_fieldsToExclude(
    TypedDict, closed=True
):
    fieldsToExclude: (
        "aws_sdk_bedrock_agent_runtime.types.fields_for_reranking.FieldsForReranking"
    )


RerankingMetadataSelectiveModeConfiguration: TypeAlias = (
    _RerankingMetadataSelectiveModeConfiguration_fieldsToInclude
    | _RerankingMetadataSelectiveModeConfiguration_fieldsToExclude
)


# --- restJson1 ser/de ---
def serialize_json(value: RerankingMetadataSelectiveModeConfiguration) -> dict:
    if "fieldsToInclude" in value:
        import aws_sdk_bedrock_agent_runtime.types.fields_for_reranking

        return {
            "fieldsToInclude": aws_sdk_bedrock_agent_runtime.types.fields_for_reranking.serialize_json(
                value["fieldsToInclude"]
            )
        }
    elif "fieldsToExclude" in value:
        import aws_sdk_bedrock_agent_runtime.types.fields_for_reranking

        return {
            "fieldsToExclude": aws_sdk_bedrock_agent_runtime.types.fields_for_reranking.serialize_json(
                value["fieldsToExclude"]
            )
        }
    else:
        raise SerializationError(
            "RerankingMetadataSelectiveModeConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RerankingMetadataSelectiveModeConfiguration:
    if "fieldsToInclude" in data:
        import aws_sdk_bedrock_agent_runtime.types.fields_for_reranking

        return {
            "fieldsToInclude": aws_sdk_bedrock_agent_runtime.types.fields_for_reranking.deserialize_json(
                data["fieldsToInclude"]
            )
        }
    elif "fieldsToExclude" in data:
        import aws_sdk_bedrock_agent_runtime.types.fields_for_reranking

        return {
            "fieldsToExclude": aws_sdk_bedrock_agent_runtime.types.fields_for_reranking.deserialize_json(
                data["fieldsToExclude"]
            )
        }
    else:
        raise DeserializationError(
            "RerankingMetadataSelectiveModeConfiguration: no recognized variant key"
        )
