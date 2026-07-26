"""Generated from Smithy shape ``com.amazonaws.configservice#EvaluationResultQualifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.base_resource_id
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.evaluation_mode
    import capo_config_service.types.string_with_char_limit256


class EvaluationResultQualifier(TypedDict, closed=True):
    config_rule_name: NotRequired[
        "capo_config_service.types.config_rule_name.ConfigRuleName"
    ]
    """<p>The name of the Config rule that was used in the evaluation.</p>"""
    resource_type: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The type of Amazon Web Services resource that was evaluated.</p>"""
    resource_id: NotRequired[
        "capo_config_service.types.base_resource_id.BaseResourceId"
    ]
    """<p>The ID of the evaluated Amazon Web Services resource.</p>"""
    evaluation_mode: NotRequired[
        "capo_config_service.types.evaluation_mode.EvaluationMode"
    ]
    """<p>The mode of an evaluation. The valid values are Detective or Proactive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationResultQualifier) -> dict:
    out: dict = {}
    if "config_rule_name" in value:
        out["ConfigRuleName"] = value["config_rule_name"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "evaluation_mode" in value:
        import capo_config_service.types.evaluation_mode

        out["EvaluationMode"] = (
            capo_config_service.types.evaluation_mode.serialize_aws_json_1_1(
                value["evaluation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationResultQualifier:
    out: EvaluationResultQualifier = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "EvaluationMode" in data:
        import capo_config_service.types.evaluation_mode

        out["evaluation_mode"] = (
            capo_config_service.types.evaluation_mode.deserialize_aws_json_1_1(
                data["EvaluationMode"]
            )
        )
    return out
