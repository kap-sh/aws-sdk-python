"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.actions
    import capo_elastic_load_balancing_v2.types.is_default
    import capo_elastic_load_balancing_v2.types.rule_arn
    import capo_elastic_load_balancing_v2.types.rule_condition_list
    import capo_elastic_load_balancing_v2.types.rule_transform_list
    import capo_elastic_load_balancing_v2.types.string


class Rule(TypedDict, closed=True):
    rule_arn: NotRequired["capo_elastic_load_balancing_v2.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    priority: NotRequired["capo_elastic_load_balancing_v2.types.string.String"]
    """<p>The priority.</p>"""
    conditions: NotRequired[
        "capo_elastic_load_balancing_v2.types.rule_condition_list.RuleConditionList"
    ]
    """<p>The conditions. Each rule can include zero or one of the following conditions: <code>http-request-method</code>, <code>host-header</code>, <code>path-pattern</code>, and <code>source-ip</code>, and zero or more of the following conditions: <code>http-header</code> and <code>query-string</code>.</p>"""
    actions: NotRequired["capo_elastic_load_balancing_v2.types.actions.Actions"]
    """<p>The actions. Each rule must include exactly one of the following types of actions: <code>forward</code>, <code>redirect</code>, or <code>fixed-response</code>, and it must be the last action to be performed.</p>"""
    is_default: NotRequired["capo_elastic_load_balancing_v2.types.is_default.IsDefault"]
    """<p>Indicates whether this is the default rule.</p>"""
    transforms: NotRequired[
        "capo_elastic_load_balancing_v2.types.rule_transform_list.RuleTransformList"
    ]
    """<p>The transforms for the rule.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Rule, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "rule_arn" in value:
        pairs.append((f"{prefix}.RuleArn", str(value["rule_arn"])))
    if "priority" in value:
        pairs.append((f"{prefix}.Priority", str(value["priority"])))
    if "conditions" in value:
        import capo_elastic_load_balancing_v2.types.rule_condition_list

        capo_elastic_load_balancing_v2.types.rule_condition_list.serialize_query(
            value["conditions"], pairs, f"{prefix}.Conditions"
        )
    if "actions" in value:
        import capo_elastic_load_balancing_v2.types.actions

        capo_elastic_load_balancing_v2.types.actions.serialize_query(
            value["actions"], pairs, f"{prefix}.Actions"
        )
    if "is_default" in value:
        pairs.append(
            (f"{prefix}.IsDefault", "true" if value["is_default"] else "false")
        )
    if "transforms" in value:
        import capo_elastic_load_balancing_v2.types.rule_transform_list

        capo_elastic_load_balancing_v2.types.rule_transform_list.serialize_query(
            value["transforms"], pairs, f"{prefix}.Transforms"
        )


def deserialize_query(el: Element) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    child_rule_arn = el.find("RuleArn")
    if child_rule_arn is not None:
        out["rule_arn"] = str(child_rule_arn.text or "")
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = str(child_priority.text or "")
    child_conditions = el.find("Conditions")
    if child_conditions is not None:
        import capo_elastic_load_balancing_v2.types.rule_condition_list

        out["conditions"] = (
            capo_elastic_load_balancing_v2.types.rule_condition_list.deserialize_query(
                child_conditions
            )
        )
    child_actions = el.find("Actions")
    if child_actions is not None:
        import capo_elastic_load_balancing_v2.types.actions

        out["actions"] = capo_elastic_load_balancing_v2.types.actions.deserialize_query(
            child_actions
        )
    child_is_default = el.find("IsDefault")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    child_transforms = el.find("Transforms")
    if child_transforms is not None:
        import capo_elastic_load_balancing_v2.types.rule_transform_list

        out["transforms"] = (
            capo_elastic_load_balancing_v2.types.rule_transform_list.deserialize_query(
                child_transforms
            )
        )
    return out
