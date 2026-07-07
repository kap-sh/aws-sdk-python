"""Generated from Smithy shape ``com.amazonaws.datazone#ListRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_type_identifiers
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_ids
    import aws_sdk_datazone.types.rule_action
    import aws_sdk_datazone.types.rule_target_type
    import aws_sdk_datazone.types.rule_type


class ListRulesInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which the rules are to be listed.</p>"""
    target_type: "aws_sdk_datazone.types.rule_target_type.RuleTargetType"
    """<p>The target type of the rule.</p>"""
    target_identifier: "str"
    """<p>The target ID of the rule.</p>"""
    rule_type: NotRequired["aws_sdk_datazone.types.rule_type.RuleType"]
    """<p>The type of the rule.</p>"""
    action: NotRequired["aws_sdk_datazone.types.rule_action.RuleAction"]
    """<p>The action of the rule.</p>"""
    project_ids: NotRequired["aws_sdk_datazone.types.project_ids.ProjectIds"]
    """<p>The IDs of projects in which rules are to be listed.</p>"""
    asset_types: NotRequired[
        "aws_sdk_datazone.types.asset_type_identifiers.AssetTypeIdentifiers"
    ]
    """<p>The asset types of the rule.</p>"""
    data_product: NotRequired["bool"]
    """<p>The data product of the rule.</p>"""
    include_cascaded: NotRequired["bool"]
    """<p>Specifies whether to include cascading rules in the results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of rules to return in a single call to <code>ListRules</code>. When the number of rules to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListRules</code> to list the next set of rules.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of rules is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of rules, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListRules</code> to list the next set of rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRulesInput:
    out: ListRulesInput = {}  # type: ignore[typeddict-item]
    return out
