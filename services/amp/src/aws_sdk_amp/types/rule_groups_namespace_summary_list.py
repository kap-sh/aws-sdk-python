"""Generated from Smithy shape ``com.amazonaws.amp#RuleGroupsNamespaceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amp.types.rule_groups_namespace_summary

RuleGroupsNamespaceSummaryList: TypeAlias = list[
    "aws_sdk_amp.types.rule_groups_namespace_summary.RuleGroupsNamespaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupsNamespaceSummaryList) -> list:
    import aws_sdk_amp.types.rule_groups_namespace_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_amp.types.rule_groups_namespace_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleGroupsNamespaceSummaryList:
    import aws_sdk_amp.types.rule_groups_namespace_summary

    out: RuleGroupsNamespaceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_amp.types.rule_groups_namespace_summary.deserialize_json(item)
        )
    return out
