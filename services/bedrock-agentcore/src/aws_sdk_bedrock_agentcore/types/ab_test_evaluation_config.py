"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestEvaluationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.online_evaluation_config_arn
    import aws_sdk_bedrock_agentcore.types.per_variant_online_evaluation_config_list


class _ABTestEvaluationConfig_onlineEvaluationConfigArn(TypedDict, closed=True):
    onlineEvaluationConfigArn: "aws_sdk_bedrock_agentcore.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"


class _ABTestEvaluationConfig_perVariantOnlineEvaluationConfig(TypedDict, closed=True):
    perVariantOnlineEvaluationConfig: "aws_sdk_bedrock_agentcore.types.per_variant_online_evaluation_config_list.PerVariantOnlineEvaluationConfigList"


ABTestEvaluationConfig: TypeAlias = (
    _ABTestEvaluationConfig_onlineEvaluationConfigArn
    | _ABTestEvaluationConfig_perVariantOnlineEvaluationConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: ABTestEvaluationConfig) -> dict:
    if "onlineEvaluationConfigArn" in value:
        return {"onlineEvaluationConfigArn": value["onlineEvaluationConfigArn"]}
    elif "perVariantOnlineEvaluationConfig" in value:
        import aws_sdk_bedrock_agentcore.types.per_variant_online_evaluation_config_list

        return {
            "perVariantOnlineEvaluationConfig": aws_sdk_bedrock_agentcore.types.per_variant_online_evaluation_config_list.serialize_json(
                value["perVariantOnlineEvaluationConfig"]
            )
        }
    else:
        raise SerializationError("ABTestEvaluationConfig: no variant present")


def deserialize_json(data: dict) -> ABTestEvaluationConfig:
    if "onlineEvaluationConfigArn" in data:
        return {"onlineEvaluationConfigArn": data["onlineEvaluationConfigArn"]}
    elif "perVariantOnlineEvaluationConfig" in data:
        import aws_sdk_bedrock_agentcore.types.per_variant_online_evaluation_config_list

        return {
            "perVariantOnlineEvaluationConfig": aws_sdk_bedrock_agentcore.types.per_variant_online_evaluation_config_list.deserialize_json(
                data["perVariantOnlineEvaluationConfig"]
            )
        }
    else:
        raise DeserializationError("ABTestEvaluationConfig: no recognized variant key")
