"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListSubCheckRuleResultsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.next_token
    import capo_ssm_sap.types.rule_result_list


class ListSubCheckRuleResultsOutput(TypedDict, closed=True):
    rule_results: NotRequired["capo_ssm_sap.types.rule_result_list.RuleResultList"]
    """<p>The rule results of a sub-check belonging to a configuration check operation.</p>"""
    next_token: NotRequired["capo_ssm_sap.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubCheckRuleResultsOutput) -> dict:
    out: dict = {}
    if "rule_results" in value:
        import capo_ssm_sap.types.rule_result_list

        out["RuleResults"] = capo_ssm_sap.types.rule_result_list.serialize_json(
            value["rule_results"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubCheckRuleResultsOutput:
    out: ListSubCheckRuleResultsOutput = {}  # type: ignore[typeddict-item]
    if "RuleResults" in data:
        import capo_ssm_sap.types.rule_result_list

        out["rule_results"] = capo_ssm_sap.types.rule_result_list.deserialize_json(
            data["RuleResults"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
