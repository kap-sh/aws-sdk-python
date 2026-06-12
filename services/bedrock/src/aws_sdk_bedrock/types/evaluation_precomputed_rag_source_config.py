"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationPrecomputedRagSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config
    import aws_sdk_bedrock.types.evaluation_precomputed_retrieve_source_config


class _EvaluationPrecomputedRagSourceConfig_retrieveSourceConfig(TypedDict):
    retrieveSourceConfig: "aws_sdk_bedrock.types.evaluation_precomputed_retrieve_source_config.EvaluationPrecomputedRetrieveSourceConfig"


class _EvaluationPrecomputedRagSourceConfig_retrieveAndGenerateSourceConfig(TypedDict):
    retrieveAndGenerateSourceConfig: "aws_sdk_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config.EvaluationPrecomputedRetrieveAndGenerateSourceConfig"


EvaluationPrecomputedRagSourceConfig: TypeAlias = (
    _EvaluationPrecomputedRagSourceConfig_retrieveSourceConfig
    | _EvaluationPrecomputedRagSourceConfig_retrieveAndGenerateSourceConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationPrecomputedRagSourceConfig) -> dict:
    if "retrieveSourceConfig" in value:
        import aws_sdk_bedrock.types.evaluation_precomputed_retrieve_source_config

        return {
            "retrieveSourceConfig": aws_sdk_bedrock.types.evaluation_precomputed_retrieve_source_config.serialize_json(
                value["retrieveSourceConfig"]
            )
        }
    elif "retrieveAndGenerateSourceConfig" in value:
        import aws_sdk_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config

        return {
            "retrieveAndGenerateSourceConfig": aws_sdk_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config.serialize_json(
                value["retrieveAndGenerateSourceConfig"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationPrecomputedRagSourceConfig: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationPrecomputedRagSourceConfig:
    if "retrieveSourceConfig" in data:
        import aws_sdk_bedrock.types.evaluation_precomputed_retrieve_source_config

        return {
            "retrieveSourceConfig": aws_sdk_bedrock.types.evaluation_precomputed_retrieve_source_config.deserialize_json(
                data["retrieveSourceConfig"]
            )
        }
    elif "retrieveAndGenerateSourceConfig" in data:
        import aws_sdk_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config

        return {
            "retrieveAndGenerateSourceConfig": aws_sdk_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config.deserialize_json(
                data["retrieveAndGenerateSourceConfig"]
            )
        }
    else:
        raise DeserializationError(
            "EvaluationPrecomputedRagSourceConfig: no recognized variant key"
        )
