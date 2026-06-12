"""Generated from Smithy shape ``com.amazonaws.configservice#StartConfigRulesEvaluationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.reevaluate_config_rule_names


class StartConfigRulesEvaluationRequest(TypedDict):
    config_rule_names: NotRequired[
        "aws_sdk_config_service.types.reevaluate_config_rule_names.ReevaluateConfigRuleNames"
    ]
    """<p>The list of names of Config rules that you want to run evaluations for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartConfigRulesEvaluationRequest) -> dict:
    out: dict = {}
    if "config_rule_names" in value:
        import aws_sdk_config_service.types.reevaluate_config_rule_names

        out["ConfigRuleNames"] = (
            aws_sdk_config_service.types.reevaluate_config_rule_names.serialize_aws_json_1_1(
                value["config_rule_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartConfigRulesEvaluationRequest:
    out: StartConfigRulesEvaluationRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRuleNames" in data:
        import aws_sdk_config_service.types.reevaluate_config_rule_names

        out["config_rule_names"] = (
            aws_sdk_config_service.types.reevaluate_config_rule_names.deserialize_aws_json_1_1(
                data["ConfigRuleNames"]
            )
        )
    return out
