"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.config_rule_state
    import capo_config_service.types.emptiable_string_with_char_limit256
    import capo_config_service.types.evaluation_modes
    import capo_config_service.types.maximum_execution_frequency
    import capo_config_service.types.rule_evaluation_visibility
    import capo_config_service.types.scope
    import capo_config_service.types.source
    import capo_config_service.types.string_with_char_limit64
    import capo_config_service.types.string_with_char_limit256
    import capo_config_service.types.string_with_char_limit1024


class ConfigRule(TypedDict, closed=True):
    config_rule_name: NotRequired[
        "capo_config_service.types.config_rule_name.ConfigRuleName"
    ]
    """<p>The name that you assign to the Config rule. The name is required if you are adding a new rule.</p>"""
    config_rule_arn: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The Amazon Resource Name (ARN) of the Config rule.</p>"""
    config_rule_id: NotRequired[
        "capo_config_service.types.string_with_char_limit64.StringWithCharLimit64"
    ]
    """<p>The ID of the Config rule.</p>"""
    description: NotRequired[
        "capo_config_service.types.emptiable_string_with_char_limit256.EmptiableStringWithCharLimit256"
    ]
    """<p>The description that you provide for the Config rule.</p>"""
    scope: NotRequired["capo_config_service.types.scope.Scope"]
    """<p>Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.</p>"""
    source: "capo_config_service.types.source.Source"
    """<p>Provides the rule owner (<code>Amazon Web Services</code> for managed rules, <code>CUSTOM_POLICY</code> for Custom Policy rules, and <code>CUSTOM_LAMBDA</code> for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your Amazon Web Services resources.</p>"""
    input_parameters: NotRequired[
        "capo_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>A string, in JSON format, that is passed to the Config rule Lambda function.</p>"""
    maximum_execution_frequency: NotRequired[
        "capo_config_service.types.maximum_execution_frequency.MaximumExecutionFrequency"
    ]
    """<p>The maximum frequency with which Config runs evaluations for a rule. You can specify a value for <code>MaximumExecutionFrequency</code> when:</p> <ul> <li> <p>This is for an Config managed rule that is triggered at a periodic frequency.</p> </li> <li> <p>Your custom rule is triggered when Config delivers the configuration snapshot. For more information, see <a>ConfigSnapshotDeliveryProperties</a>.</p> </li> </ul> <note> <p>By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the <code>MaximumExecutionFrequency</code> parameter.</p> </note>"""
    config_rule_state: NotRequired[
        "capo_config_service.types.config_rule_state.ConfigRuleState"
    ]
    """<p>Indicates whether the Config rule is active or is currently being deleted by Config. It can also indicate the evaluation status for the Config rule.</p> <p>Config sets the state of the rule to <code>EVALUATING</code> temporarily after you use the <code>StartConfigRulesEvaluation</code> request to evaluate your resources against the Config rule.</p> <p>Config sets the state of the rule to <code>DELETING_RESULTS</code> temporarily after you use the <code>DeleteEvaluationResults</code> request to delete the current evaluation results for the Config rule.</p> <p>Config temporarily sets the state of a rule to <code>DELETING</code> after you use the <code>DeleteConfigRule</code> request to delete the rule. After Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.</p>"""
    created_by: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Service principal name of the service that created the rule.</p> <note> <p>The field is populated only if the service-linked rule is created by a service. The field is empty if you create your own rule.</p> </note>"""
    evaluation_modes: NotRequired[
        "capo_config_service.types.evaluation_modes.EvaluationModes"
    ]
    """<p>The modes the Config rule can be evaluated in. The valid values are distinct objects. By default, the value is Detective evaluation mode only.</p>"""
    rule_evaluation_visibility: NotRequired[
        "capo_config_service.types.rule_evaluation_visibility.RuleEvaluationVisibility"
    ]
    """<p>Indicates whether you can get <a>Evaluation</a>s for the Config rule. You can get <a>Evaluation</a>s for the Amazon Web Services Config rule if this value is <code>EXTERNAL</code>. You cannot get <a>Evaluation</a>s for the Amazon Web Services Config rule if this value is <code>INTERNAL</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigRule) -> dict:
    out: dict = {}
    if "config_rule_name" in value:
        out["ConfigRuleName"] = value["config_rule_name"]
    if "config_rule_arn" in value:
        out["ConfigRuleArn"] = value["config_rule_arn"]
    if "config_rule_id" in value:
        out["ConfigRuleId"] = value["config_rule_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "scope" in value:
        import capo_config_service.types.scope

        out["Scope"] = capo_config_service.types.scope.serialize_aws_json_1_1(
            value["scope"]
        )
    import capo_config_service.types.source

    out["Source"] = capo_config_service.types.source.serialize_aws_json_1_1(
        value["source"]
    )
    if "input_parameters" in value:
        out["InputParameters"] = value["input_parameters"]
    if "maximum_execution_frequency" in value:
        import capo_config_service.types.maximum_execution_frequency

        out["MaximumExecutionFrequency"] = (
            capo_config_service.types.maximum_execution_frequency.serialize_aws_json_1_1(
                value["maximum_execution_frequency"]
            )
        )
    if "config_rule_state" in value:
        import capo_config_service.types.config_rule_state

        out["ConfigRuleState"] = (
            capo_config_service.types.config_rule_state.serialize_aws_json_1_1(
                value["config_rule_state"]
            )
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "evaluation_modes" in value:
        import capo_config_service.types.evaluation_modes

        out["EvaluationModes"] = (
            capo_config_service.types.evaluation_modes.serialize_aws_json_1_1(
                value["evaluation_modes"]
            )
        )
    if "rule_evaluation_visibility" in value:
        import capo_config_service.types.rule_evaluation_visibility

        out["RuleEvaluationVisibility"] = (
            capo_config_service.types.rule_evaluation_visibility.serialize_aws_json_1_1(
                value["rule_evaluation_visibility"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigRule:
    out: ConfigRule = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    if "ConfigRuleArn" in data:
        out["config_rule_arn"] = data["ConfigRuleArn"]
    if "ConfigRuleId" in data:
        out["config_rule_id"] = data["ConfigRuleId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Scope" in data:
        import capo_config_service.types.scope

        out["scope"] = capo_config_service.types.scope.deserialize_aws_json_1_1(
            data["Scope"]
        )
    if "Source" in data:
        import capo_config_service.types.source

        out["source"] = capo_config_service.types.source.deserialize_aws_json_1_1(
            data["Source"]
        )
    else:
        raise DeserializationError("ConfigRule.source required")
    if "InputParameters" in data:
        out["input_parameters"] = data["InputParameters"]
    if "MaximumExecutionFrequency" in data:
        import capo_config_service.types.maximum_execution_frequency

        out["maximum_execution_frequency"] = (
            capo_config_service.types.maximum_execution_frequency.deserialize_aws_json_1_1(
                data["MaximumExecutionFrequency"]
            )
        )
    if "ConfigRuleState" in data:
        import capo_config_service.types.config_rule_state

        out["config_rule_state"] = (
            capo_config_service.types.config_rule_state.deserialize_aws_json_1_1(
                data["ConfigRuleState"]
            )
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "EvaluationModes" in data:
        import capo_config_service.types.evaluation_modes

        out["evaluation_modes"] = (
            capo_config_service.types.evaluation_modes.deserialize_aws_json_1_1(
                data["EvaluationModes"]
            )
        )
    if "RuleEvaluationVisibility" in data:
        import capo_config_service.types.rule_evaluation_visibility

        out["rule_evaluation_visibility"] = (
            capo_config_service.types.rule_evaluation_visibility.deserialize_aws_json_1_1(
                data["RuleEvaluationVisibility"]
            )
        )
    return out
