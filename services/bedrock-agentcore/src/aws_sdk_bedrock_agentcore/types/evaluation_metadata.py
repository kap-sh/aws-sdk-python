"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.session_metadata_list


class _EvaluationMetadata_sessionMetadata(TypedDict, closed=True):
    sessionMetadata: (
        "aws_sdk_bedrock_agentcore.types.session_metadata_list.SessionMetadataList"
    )


EvaluationMetadata: TypeAlias = _EvaluationMetadata_sessionMetadata


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationMetadata) -> dict:
    if "sessionMetadata" in value:
        import aws_sdk_bedrock_agentcore.types.session_metadata_list

        return {
            "sessionMetadata": aws_sdk_bedrock_agentcore.types.session_metadata_list.serialize_json(
                value["sessionMetadata"]
            )
        }
    else:
        raise SerializationError("EvaluationMetadata: no variant present")


def deserialize_json(data: dict) -> EvaluationMetadata:
    if "sessionMetadata" in data:
        import aws_sdk_bedrock_agentcore.types.session_metadata_list

        return {
            "sessionMetadata": aws_sdk_bedrock_agentcore.types.session_metadata_list.deserialize_json(
                data["sessionMetadata"]
            )
        }
    else:
        raise DeserializationError("EvaluationMetadata: no recognized variant key")
