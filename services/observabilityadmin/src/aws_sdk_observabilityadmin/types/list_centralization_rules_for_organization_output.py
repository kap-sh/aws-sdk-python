"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListCentralizationRulesForOrganizationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.centralization_rule_summaries
    import aws_sdk_observabilityadmin.types.next_token


class ListCentralizationRulesForOrganizationOutput(TypedDict):
    centralization_rule_summaries: NotRequired[
        "aws_sdk_observabilityadmin.types.centralization_rule_summaries.CentralizationRuleSummaries"
    ]
    """<p>A list of centralization rule summaries.</p>"""
    next_token: NotRequired["aws_sdk_observabilityadmin.types.next_token.NextToken"]
    """<p>A token to resume pagination of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCentralizationRulesForOrganizationOutput) -> dict:
    out: dict = {}
    if "centralization_rule_summaries" in value:
        import aws_sdk_observabilityadmin.types.centralization_rule_summaries

        out["CentralizationRuleSummaries"] = (
            aws_sdk_observabilityadmin.types.centralization_rule_summaries.serialize_json(
                value["centralization_rule_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCentralizationRulesForOrganizationOutput:
    out: ListCentralizationRulesForOrganizationOutput = {}  # type: ignore[typeddict-item]
    if "CentralizationRuleSummaries" in data:
        import aws_sdk_observabilityadmin.types.centralization_rule_summaries

        out["centralization_rule_summaries"] = (
            aws_sdk_observabilityadmin.types.centralization_rule_summaries.deserialize_json(
                data["CentralizationRuleSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
