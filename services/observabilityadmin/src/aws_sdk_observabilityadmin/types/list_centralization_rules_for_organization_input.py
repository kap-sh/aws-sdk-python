"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListCentralizationRulesForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.list_centralization_rules_for_organization_max_results
    import aws_sdk_observabilityadmin.types.next_token


class ListCentralizationRulesForOrganizationInput(TypedDict, closed=True):
    rule_name_prefix: NotRequired["str"]
    """<p>A string to filter organization centralization rules whose names begin with the specified prefix.</p>"""
    all_regions: NotRequired["bool"]
    """<p>A flag determining whether to return organization centralization rules from all regions or only the current region.</p>"""
    max_results: NotRequired[
        "aws_sdk_observabilityadmin.types.list_centralization_rules_for_organization_max_results.ListCentralizationRulesForOrganizationMaxResults"
    ]
    """<p>The maximum number of organization centralization rules to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_observabilityadmin.types.next_token.NextToken"]
    """<p>The token for the next set of results. A previous call generates this token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCentralizationRulesForOrganizationInput) -> dict:
    out: dict = {}
    if "rule_name_prefix" in value:
        out["RuleNamePrefix"] = value["rule_name_prefix"]
    if "all_regions" in value:
        out["AllRegions"] = value["all_regions"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCentralizationRulesForOrganizationInput:
    out: ListCentralizationRulesForOrganizationInput = {}  # type: ignore[typeddict-item]
    if "RuleNamePrefix" in data:
        out["rule_name_prefix"] = data["RuleNamePrefix"]
    if "AllRegions" in data:
        out["all_regions"] = data["AllRegions"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
