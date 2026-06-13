"""Generated from Smithy shape ``com.amazonaws.amp#DescribeRuleGroupsNamespaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.rule_groups_namespace_description


class DescribeRuleGroupsNamespaceResponse(TypedDict):
    rule_groups_namespace: "aws_sdk_amp.types.rule_groups_namespace_description.RuleGroupsNamespaceDescription"
    """<p>The information about the rule groups namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRuleGroupsNamespaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.rule_groups_namespace_description

    out["ruleGroupsNamespace"] = (
        aws_sdk_amp.types.rule_groups_namespace_description.serialize_json(
            value["rule_groups_namespace"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeRuleGroupsNamespaceResponse:
    out: DescribeRuleGroupsNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "ruleGroupsNamespace" in data:
        import aws_sdk_amp.types.rule_groups_namespace_description

        out["rule_groups_namespace"] = (
            aws_sdk_amp.types.rule_groups_namespace_description.deserialize_json(
                data["ruleGroupsNamespace"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeRuleGroupsNamespaceResponse.rule_groups_namespace required"
        )
    return out
