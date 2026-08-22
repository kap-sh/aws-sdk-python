"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PerVariantOnlineEvaluationConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.per_variant_online_evaluation_config

PerVariantOnlineEvaluationConfigList: TypeAlias = list[
    "capo_bedrock_agentcore.types.per_variant_online_evaluation_config.PerVariantOnlineEvaluationConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: PerVariantOnlineEvaluationConfigList) -> list:
    import capo_bedrock_agentcore.types.per_variant_online_evaluation_config

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.per_variant_online_evaluation_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PerVariantOnlineEvaluationConfigList:
    import capo_bedrock_agentcore.types.per_variant_online_evaluation_config

    out: PerVariantOnlineEvaluationConfigList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.per_variant_online_evaluation_config.deserialize_json(
                item
            )
        )
    return out
