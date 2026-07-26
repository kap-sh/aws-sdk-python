"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationRulePreviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.criteria
    import capo_compute_optimizer_automation.types.next_token
    import capo_compute_optimizer_automation.types.organization_scope
    import capo_compute_optimizer_automation.types.recommended_action_type_list
    import capo_compute_optimizer_automation.types.rule_type


class ListAutomationRulePreviewRequest(TypedDict, closed=True):
    rule_type: "capo_compute_optimizer_automation.types.rule_type.RuleType"
    """<p> The type of rule. </p> <note> <p>Only the management account or a delegated administrator can set the ruleType to be OrganizationRule.</p> </note>"""
    organization_scope: NotRequired[
        "capo_compute_optimizer_automation.types.organization_scope.OrganizationScope"
    ]
    """<p> The organizational scope for the rule preview. </p>"""
    recommended_action_types: "capo_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
    """<p> The types of recommended actions to include in the preview. </p>"""
    criteria: NotRequired["capo_compute_optimizer_automation.types.criteria.Criteria"]
    """<p>A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of automation rule preview results to return in a single response. Valid range is 1-1000.</p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationRulePreviewRequest) -> dict:
    out: dict = {}
    import capo_compute_optimizer_automation.types.rule_type

    out["ruleType"] = (
        capo_compute_optimizer_automation.types.rule_type.serialize_aws_json_1_0(
            value["rule_type"]
        )
    )
    if "organization_scope" in value:
        import capo_compute_optimizer_automation.types.organization_scope

        out["organizationScope"] = (
            capo_compute_optimizer_automation.types.organization_scope.serialize_aws_json_1_0(
                value["organization_scope"]
            )
        )
    import capo_compute_optimizer_automation.types.recommended_action_type_list

    out["recommendedActionTypes"] = (
        capo_compute_optimizer_automation.types.recommended_action_type_list.serialize_aws_json_1_0(
            value["recommended_action_types"]
        )
    )
    if "criteria" in value:
        import capo_compute_optimizer_automation.types.criteria

        out["criteria"] = (
            capo_compute_optimizer_automation.types.criteria.serialize_aws_json_1_0(
                value["criteria"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationRulePreviewRequest:
    out: ListAutomationRulePreviewRequest = {}  # type: ignore[typeddict-item]
    if "ruleType" in data:
        import capo_compute_optimizer_automation.types.rule_type

        out["rule_type"] = (
            capo_compute_optimizer_automation.types.rule_type.deserialize_aws_json_1_0(
                data["ruleType"]
            )
        )
    else:
        raise DeserializationError(
            "ListAutomationRulePreviewRequest.rule_type required"
        )
    if "organizationScope" in data:
        import capo_compute_optimizer_automation.types.organization_scope

        out["organization_scope"] = (
            capo_compute_optimizer_automation.types.organization_scope.deserialize_aws_json_1_0(
                data["organizationScope"]
            )
        )
    if "recommendedActionTypes" in data:
        import capo_compute_optimizer_automation.types.recommended_action_type_list

        out["recommended_action_types"] = (
            capo_compute_optimizer_automation.types.recommended_action_type_list.deserialize_aws_json_1_0(
                data["recommendedActionTypes"]
            )
        )
    else:
        raise DeserializationError(
            "ListAutomationRulePreviewRequest.recommended_action_types required"
        )
    if "criteria" in data:
        import capo_compute_optimizer_automation.types.criteria

        out["criteria"] = (
            capo_compute_optimizer_automation.types.criteria.deserialize_aws_json_1_0(
                data["criteria"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
