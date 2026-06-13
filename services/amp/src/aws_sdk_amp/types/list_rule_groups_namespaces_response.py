"""Generated from Smithy shape ``com.amazonaws.amp#ListRuleGroupsNamespacesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.pagination_token
    import aws_sdk_amp.types.rule_groups_namespace_summary_list


class ListRuleGroupsNamespacesResponse(TypedDict):
    rule_groups_namespaces: "aws_sdk_amp.types.rule_groups_namespace_summary_list.RuleGroupsNamespaceSummaryList"
    """<p>The returned list of rule groups namespaces.</p>"""
    next_token: NotRequired["aws_sdk_amp.types.pagination_token.PaginationToken"]
    """<p>A token indicating that there are more results to retrieve. You can use this token as part of your next <code>ListRuleGroupsNamespaces</code> request to retrieve those results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRuleGroupsNamespacesResponse) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.rule_groups_namespace_summary_list

    out["ruleGroupsNamespaces"] = (
        aws_sdk_amp.types.rule_groups_namespace_summary_list.serialize_json(
            value["rule_groups_namespaces"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRuleGroupsNamespacesResponse:
    out: ListRuleGroupsNamespacesResponse = {}  # type: ignore[typeddict-item]
    if "ruleGroupsNamespaces" in data:
        import aws_sdk_amp.types.rule_groups_namespace_summary_list

        out["rule_groups_namespaces"] = (
            aws_sdk_amp.types.rule_groups_namespace_summary_list.deserialize_json(
                data["ruleGroupsNamespaces"]
            )
        )
    else:
        raise DeserializationError(
            "ListRuleGroupsNamespacesResponse.rule_groups_namespaces required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
