"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PerVariantOnlineEvaluationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.online_evaluation_config_arn
    import capo_bedrock_agentcore.types.variant_name


class PerVariantOnlineEvaluationConfig(TypedDict, closed=True):
    name: "capo_bedrock_agentcore.types.variant_name.VariantName"
    """<p>The name of the variant this evaluation configuration applies to.</p>"""
    online_evaluation_config_arn: "capo_bedrock_agentcore.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p>The Amazon Resource Name (ARN) of the online evaluation configuration for this variant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerVariantOnlineEvaluationConfig) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    return out


def deserialize_json(data: dict) -> PerVariantOnlineEvaluationConfig:
    out: PerVariantOnlineEvaluationConfig = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PerVariantOnlineEvaluationConfig.name required")
    if "onlineEvaluationConfigArn" in data:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        raise DeserializationError(
            "PerVariantOnlineEvaluationConfig.online_evaluation_config_arn required"
        )
    return out
