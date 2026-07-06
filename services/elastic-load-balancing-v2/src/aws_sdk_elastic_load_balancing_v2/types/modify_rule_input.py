"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.actions
    import aws_sdk_elastic_load_balancing_v2.types.reset_transforms
    import aws_sdk_elastic_load_balancing_v2.types.rule_arn
    import aws_sdk_elastic_load_balancing_v2.types.rule_condition_list
    import aws_sdk_elastic_load_balancing_v2.types.rule_transform_list


class ModifyRuleInput(TypedDict, closed=True):
    rule_arn: NotRequired["aws_sdk_elastic_load_balancing_v2.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    conditions: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.rule_condition_list.RuleConditionList"
    ]
    """<p>The conditions.</p>"""
    actions: NotRequired["aws_sdk_elastic_load_balancing_v2.types.actions.Actions"]
    """<p>The actions.</p>"""
    transforms: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.rule_transform_list.RuleTransformList"
    ]
    """<p>The transforms to apply to requests that match this rule. You can add one host header rewrite transform and one URL rewrite transform. If you specify <code>Transforms</code>, you can't specify <code>ResetTransforms</code>.</p>"""
    reset_transforms: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.reset_transforms.ResetTransforms"
    ]
    """<p>Indicates whether to remove all transforms from the rule. If you specify <code>ResetTransforms</code>, you can't specify <code>Transforms</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyRuleInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rule_arn" in value:
        pairs.append((f"{prefix}.RuleArn", str(value["rule_arn"])))
    if "conditions" in value:
        import aws_sdk_elastic_load_balancing_v2.types.rule_condition_list

        aws_sdk_elastic_load_balancing_v2.types.rule_condition_list.serialize_query(
            value["conditions"], pairs, f"{prefix}.Conditions"
        )
    if "actions" in value:
        import aws_sdk_elastic_load_balancing_v2.types.actions

        aws_sdk_elastic_load_balancing_v2.types.actions.serialize_query(
            value["actions"], pairs, f"{prefix}.Actions"
        )
    if "transforms" in value:
        import aws_sdk_elastic_load_balancing_v2.types.rule_transform_list

        aws_sdk_elastic_load_balancing_v2.types.rule_transform_list.serialize_query(
            value["transforms"], pairs, f"{prefix}.Transforms"
        )
    if "reset_transforms" in value:
        pairs.append(
            (
                f"{prefix}.ResetTransforms",
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
        import aws_sdk_elastic_load_balancing_v2.types.rule_condition_list

        out["conditions"] = (
            aws_sdk_elastic_load_balancing_v2.types.rule_condition_list.deserialize_query(
                child_conditions
            )
        )
    child_actions = el.find("Actions")
    if child_actions is not None:
        import aws_sdk_elastic_load_balancing_v2.types.actions

        out["actions"] = (
            aws_sdk_elastic_load_balancing_v2.types.actions.deserialize_query(
                child_actions
            )
        )
    child_transforms = el.find("Transforms")
    if child_transforms is not None:
        import aws_sdk_elastic_load_balancing_v2.types.rule_transform_list

        out["transforms"] = (
            aws_sdk_elastic_load_balancing_v2.types.rule_transform_list.deserialize_query(
                child_transforms
            )
        )
    child_reset_transforms = el.find("ResetTransforms")
    if child_reset_transforms is not None:
        out["reset_transforms"] = (child_reset_transforms.text or "").lower() == "true"
    return out
