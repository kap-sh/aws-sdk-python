"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.actions
    import aws_sdk_elastic_load_balancing_v2.types.listener_arn
    import aws_sdk_elastic_load_balancing_v2.types.rule_condition_list
    import aws_sdk_elastic_load_balancing_v2.types.rule_priority
    import aws_sdk_elastic_load_balancing_v2.types.rule_transform_list
    import aws_sdk_elastic_load_balancing_v2.types.tag_list


class CreateRuleInput(TypedDict, closed=True):
    listener_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    conditions: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.rule_condition_list.RuleConditionList"
    ]
    """<p>The conditions.</p>"""
    priority: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.rule_priority.RulePriority"
    ]
    """<p>The rule priority. A listener can't have multiple rules with the same priority.</p>"""
    actions: NotRequired["aws_sdk_elastic_load_balancing_v2.types.actions.Actions"]
    """<p>The actions.</p>"""
    tags: NotRequired["aws_sdk_elastic_load_balancing_v2.types.tag_list.TagList"]
    """<p>The tags to assign to the rule.</p>"""
    transforms: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.rule_transform_list.RuleTransformList"
    ]
    """<p>The transforms to apply to requests that match this rule. You can add one host header rewrite transform and one URL rewrite transform.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateRuleInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "listener_arn" in value:
        pairs.append((f"{prefix}.ListenerArn", str(value["listener_arn"])))
    if "conditions" in value:
        import aws_sdk_elastic_load_balancing_v2.types.rule_condition_list

        aws_sdk_elastic_load_balancing_v2.types.rule_condition_list.serialize_query(
            value["conditions"], pairs, f"{prefix}.Conditions"
        )
    if "priority" in value:
        pairs.append((f"{prefix}.Priority", str(value["priority"])))
    if "actions" in value:
        import aws_sdk_elastic_load_balancing_v2.types.actions

        aws_sdk_elastic_load_balancing_v2.types.actions.serialize_query(
            value["actions"], pairs, f"{prefix}.Actions"
        )
    if "tags" in value:
        import aws_sdk_elastic_load_balancing_v2.types.tag_list

        aws_sdk_elastic_load_balancing_v2.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "transforms" in value:
        import aws_sdk_elastic_load_balancing_v2.types.rule_transform_list

        aws_sdk_elastic_load_balancing_v2.types.rule_transform_list.serialize_query(
            value["transforms"], pairs, f"{prefix}.Transforms"
        )


def deserialize_query(el: Element) -> CreateRuleInput:
    out: CreateRuleInput = {}  # type: ignore[typeddict-item]
    child_listener_arn = el.find("ListenerArn")
    if child_listener_arn is not None:
        out["listener_arn"] = str(child_listener_arn.text or "")
    child_conditions = el.find("Conditions")
    if child_conditions is not None:
        import aws_sdk_elastic_load_balancing_v2.types.rule_condition_list

        out["conditions"] = (
            aws_sdk_elastic_load_balancing_v2.types.rule_condition_list.deserialize_query(
                child_conditions
            )
        )
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    child_actions = el.find("Actions")
    if child_actions is not None:
        import aws_sdk_elastic_load_balancing_v2.types.actions

        out["actions"] = (
            aws_sdk_elastic_load_balancing_v2.types.actions.deserialize_query(
                child_actions
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elastic_load_balancing_v2.types.tag_list

        out["tags"] = (
            aws_sdk_elastic_load_balancing_v2.types.tag_list.deserialize_query(
                child_tags
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
    return out
