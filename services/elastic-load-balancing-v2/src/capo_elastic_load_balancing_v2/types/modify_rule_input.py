"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.actions
    import capo_elastic_load_balancing_v2.types.reset_transforms
    import capo_elastic_load_balancing_v2.types.rule_arn
    import capo_elastic_load_balancing_v2.types.rule_condition_list
    import capo_elastic_load_balancing_v2.types.rule_transform_list


class ModifyRuleInput(TypedDict, closed=True):
    rule_arn: NotRequired["capo_elastic_load_balancing_v2.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    conditions: NotRequired[
        "capo_elastic_load_balancing_v2.types.rule_condition_list.RuleConditionList"
    ]
    """<p>The conditions.</p>"""
    actions: NotRequired["capo_elastic_load_balancing_v2.types.actions.Actions"]
    """<p>The actions.</p>"""
    transforms: NotRequired[
        "capo_elastic_load_balancing_v2.types.rule_transform_list.RuleTransformList"
    ]
    """<p>The transforms to apply to requests that match this rule. You can add one host header rewrite transform and one URL rewrite transform. If you specify <code>Transforms</code>, you can't specify <code>ResetTransforms</code>.</p>"""
    reset_transforms: NotRequired[
        "capo_elastic_load_balancing_v2.types.reset_transforms.ResetTransforms"
    ]
    """<p>Indicates whether to remove all transforms from the rule. If you specify <code>ResetTransforms</code>, you can't specify <code>Transforms</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyRuleInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule_arn" in value:
        pairs.append((f"{key_prefix}RuleArn", str(value["rule_arn"])))
    if "conditions" in value:
        import capo_elastic_load_balancing_v2.types.rule_condition_list

        capo_elastic_load_balancing_v2.types.rule_condition_list.serialize_query(
            value["conditions"], pairs, f"{key_prefix}Conditions"
        )
    if "actions" in value:
        import capo_elastic_load_balancing_v2.types.actions

        capo_elastic_load_balancing_v2.types.actions.serialize_query(
            value["actions"], pairs, f"{key_prefix}Actions"
        )
    if "transforms" in value:
        import capo_elastic_load_balancing_v2.types.rule_transform_list

        capo_elastic_load_balancing_v2.types.rule_transform_list.serialize_query(
            value["transforms"], pairs, f"{key_prefix}Transforms"
        )
    if "reset_transforms" in value:
        pairs.append(
            (
                f"{key_prefix}ResetTransforms",
                "true" if value["reset_transforms"] else "false",
            )
        )


def deserialize_query(el: Element) -> ModifyRuleInput:
    out: ModifyRuleInput = {}  # type: ignore[typeddict-item]
    child_rule_arn = el.find("RuleArn")
    if child_rule_arn is not None:
        out["rule_arn"] = str(child_rule_arn.text or "")
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
    child_transforms = el.find("Transforms")
    if child_transforms is not None:
        import capo_elastic_load_balancing_v2.types.rule_transform_list

        out["transforms"] = (
            capo_elastic_load_balancing_v2.types.rule_transform_list.deserialize_query(
                child_transforms
            )
        )
    child_reset_transforms = el.find("ResetTransforms")
    if child_reset_transforms is not None:
        out["reset_transforms"] = (child_reset_transforms.text or "").lower() == "true"
    return out
